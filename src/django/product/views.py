from rest_framework import viewsets, permissions
from .models import Category, Product, Question, Review, Answer
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    QuestionSerializer,
    ReviewSerializer,
    AnswerSerializer,
)

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permissions_classes = [permissions.IsAuthenticated]


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permissions_classes = [permissions.IsAuthenticated]


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permissions_classes = [permissions.IsAuthenticated]
