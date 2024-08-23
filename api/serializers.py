from rest_framework import serializers
from quizzes.models import Quiz, Question, UserResult

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'correct_answer', 'choices']

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'category', 'questions', 'approved']

class UserResultSerializer(serializers.ModelSerializer):
    # Thinking of not exposing userresults to the api
    class Meta:
        model = UserResult
        fields = ['id', 'user', 'quiz', 'score', 'completion_time']
