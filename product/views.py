from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Review
from .serializers import CategorySerializer, CategoryDetailSerializer, ProductSerializer, ProductDetailSerializer, ProductReviewSerializer, ReviewSerializer, ReviewDetailSerializer


@api_view(['GET'])
def category_list_api_view(request):
    list = Category.objects.all()
    data = CategorySerializer(list, many = True).data
    return Response(data = data, status = status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id = id)
    except Category.DoesNotExist:
        return Response (data = {'error': 'Page not found'}, status = status.HTTP_404_NOT_FOUND)
    data = CategoryDetailSerializer(category, many = False).data
    return Response(data = data, status = status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def product_list_api_view(request):
    list = Product.objects.all()
    data = ProductSerializer(list, many = True).data
    return Response (data = data, status = status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def product_review_api_view(request):
    list = Product.objects.all()
    data = ProductReviewSerializer(list, many = True).data
    return Response (data = data, status = status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id = id)
    except Product.DoesNotExist:
        return Response (data = {'error': 'Page not found'}, status = status.HTTP_404_NOT_FOUND)
    data = ProductDetailSerializer(product, many = False).data
    return Response (data = data, status = status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def review_list_api_view(request):
    list = Review.objects.all()
    data = ReviewSerializer(list, many = True).data
    return Response (data = data, status = status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id = id)
    except Review.DoesNotExist:
        return Response (data = {'error': 'Page not found'}, status = status.HTTP_404_NOT_FOUND)
    data = ReviewDetailSerializer(review, many = False).data
    return Response (data = data, status = status.HTTP_202_ACCEPTED)