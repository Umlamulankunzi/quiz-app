from django.urls import path
from . import views


urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/create/', views.create_quiz, name='create_quiz'),
    path('quiz/<int:quiz_id>/update/', views.update_quiz, name='update_quiz'),
    path('quiz/<int:quiz_id>/delete/', views.delete_quiz, name='delete_quiz'),
    path('quiz/<int:quiz_id>/submit/', views.submit_quiz, name='submit_quiz'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('quiz-master-dashboard/', views.quiz_master_dashboard, name='quiz_master_dashboard'),

]
