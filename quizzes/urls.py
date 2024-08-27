from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.user_dashboard, name='user_dashboard'),

    path('categories/', views.category_list, name='category_list'),
    path('select-quiz/', views.select_quiz_preferences, name='select_quiz'),
    path('quiz/start/<int:category_id>/<int:num_questions>/', views.generate_quiz, name='generate_quiz'),

    path('questions/add/', views.add_question, name='add_question'),


    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),

    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),

    path('quiz/attempt/<int:quiz_id>/', views.attempt_quiz, name='attempt_quiz'),
    path('quiz/result/<int:quiz_id>/', views.quiz_result, name='quiz_result'),


    path('attempt-quiz/', views.attempt_quiz, name='attempt_quiz')
]
