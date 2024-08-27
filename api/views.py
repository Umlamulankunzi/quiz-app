
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, permissions, pagination
from quizzes.models import Category, Question  # UserResult
from .serializers import CategorySerializer, QuestionSerializer
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


# Create your views here.
class APIRootView(APIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Category.objects.all()

    def get(self, request, format=None):
        return Response({
            'categories': reverse('category_list_api', request=request, format=format),
        })


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # pagination_class = pagination.PageNumberPagination

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # pagination_class = pagination.PageNumberPagination

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Question.objects.filter(category_id=category_id)
