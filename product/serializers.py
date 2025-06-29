from rest_framework import serializers
from .models import Category, Product, Review

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




