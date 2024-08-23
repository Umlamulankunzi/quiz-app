from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='api_home'),
    path('quizzes/', views.QuizListView.as_view(), name='quiz_list_api'),
    path('quizzes/<int:pk>/', views.QuizDetailView.as_view(), name='quiz_detail_api'),
    path('quizzes/<int:quiz_id>/submit/', views.SubmitQuizView.as_view(), name='submit_quiz_api'),
]
