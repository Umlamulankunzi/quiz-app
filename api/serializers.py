from rest_framework import serializers
from quizzes.models import Question, Category

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id', 'question_type', 'difficulty', 'category',
            'question_text', 'correct_answer', 'is_approved']

class CategorySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'questions']
