import json
import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from quizzes.models import Question, Category

class Command(BaseCommand):
    help = 'Import questions from a JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        # Read and parse the JSON file
        with open(json_file, 'r') as file:
            data = json.load(file)

        for item in data['results']:
            category_name = item['category']
            category, created = Category.objects.get_or_create(name=category_name)

            # Create or get the user (you might need to adjust this based on your actual user model)
            user = User.objects.first()  # Or get a specific user if needed

            Question.objects.create(
                question_type=item['type'],
                difficulty=item['difficulty'],
                category=category,
                question_text=item['question'],
                correct_answer=item['correct_answer'],
                incorrect_answers=item['incorrect_answers'],
                created_by=user,
                is_approved=True  # Set this based on your requirements
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported questions'))
