from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Review
from .serializers import CategorySerializer, CategoryDetailSerializer, ProductSerializer, ProductDetailSerializer, ProductReviewSerializer, ReviewSerializer, ReviewDetailSerializer
from django.db import transaction


@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        list = Category.objects.all()
        data = CategorySerializer(list, many = True).data
        return Response(data = data, status = status.HTTP_202_ACCEPTED)
    elif request.method == 'POST':
        name = request.data.get('name')
        category = Category.objects.create(name = name)
        category.save()
        return Response(data = CategoryDetailSerializer(category).data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id = id)
    except Category.DoesNotExist:
        return Response (data = {'error': 'Page not found'}, status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = CategoryDetailSerializer(category, many = False).data
        return Response(data = data, status = status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        category.name = request.data.get('name')
        category.save()
        return Response(data = CategoryDetailSerializer(category).data, status = status.HTTP_201_CREATED)
    else:
        category.delete()
        return Response (status = status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        list = Product.objects.all()
        data = ProductSerializer(list, many = True).data
        return Response (data = data, status = status.HTTP_202_ACCEPTED)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category_id')
        with transaction.atomic():
            product = Product.objects.create(
                title = title,
                description = description,
                price = price,
                category_id = category_id,
            )
            product.save()
        return Response (data = ProductDetailSerializer(product).data, status = status.HTTP_201_CREATED)

@api_view(['GET'])
def product_review_api_view(request):
    list = Product.objects.all()
    data = ProductReviewSerializer(list, many = True).data
    return Response (data = data, status = status.HTTP_202_ACCEPTED)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id = id)
    except Product.DoesNotExist:
        return Response (data = {'error': 'Page not found'}, status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ProductDetailSerializer(product, many = False).data
        return Response (data = data, status = status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        product.category_id = request.data.get('category_id')
        product.save()
        return Response (data = ProductDetailSerializer(product).data, status = status.HTTP_201_CREATED)
    else:
        product.delete()
        return Response (status = status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        list = Review.objects.all()
        data = ReviewSerializer(list, many = True).data
        return Response (data = data, status = status.HTTP_202_ACCEPTED)
    elif request.method == 'POST':
        text = request.data.get('text')
        stars = request.data.get('stars')
        product_id = request.data.get('product_id')
        with transaction.atomic():
            review = Review.objects.create(
                text = text,
                stars = stars,
                product_id = product_id,
            )
            review.save()
        return Response (data = ReviewDetailSerializer(review).data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id = id)
    except Review.DoesNotExist:
        return Response (data = {'error': 'Page not found'}, status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewDetailSerializer(review, many = False).data
        return Response (data = data, status = status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.product_id = request.data.get('product_id')
        review.save()
        return Response (data = ReviewDetailSerializer(review).data, status = status.HTTP_201_CREATED)
    else:
        review.delete()
        return Response (status = status.HTTP_204_NO_CONTENT)