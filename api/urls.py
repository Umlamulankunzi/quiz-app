from django.urls import path
from . import views

urlpatterns = [
    path('', views.APIRootView.as_view(), name='api-root'),
    path('categories/', views.CategoryListView.as_view(), name='category_list_api'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail_api'),
    path('categories/<int:category_id>/questions/', views.QuestionListView.as_view(), name='question_list'),
]
