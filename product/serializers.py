from rest_framework import serializers
from .models import Category, Product, Review
from rest_framework.exceptions import ValidationError

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title'.split()

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many = True)
    class Meta:
        model = Category
        fields = 'name products product_count'.split()

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars'.split()
    
class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class ProductDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many = True)
    class Meta:
        model = Product
        fields = 'title description price category reviews average_rating'.split()
    
class ProductReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Product
        fields = 'title description price category reviews average_rating'.split()

class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required = True, max_length = 63)

class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required = True, max_length = 63)
    description = serializers.CharField(required = False, max_length = 255)
    price = serializers.IntegerField(min_value = 1)
    category_id = serializers.IntegerField()

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id = category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exist')
        return category_id

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required = True, max_length = 255)
    stars = serializers.IntegerField(min_value = 1, max_value = 5)
    product_id = serializers.IntegerField()

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id = product_id)
        except Product.DoesNotExist:
            raise ValidationError('Product does not exist')
        return product_id



