from django.db import models
from django.contrib.auth.models import User
import random


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Question(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('multiple', 'Multiple Choice'),
        ('boolean', 'True/False'),
    ]

    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    question_type = models.CharField(max_length=10, choices=QUESTION_TYPE_CHOICES)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question_text = models.TextField()
    correct_answer = models.CharField(max_length=255)
    incorrect_answers = models.JSONField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.question_text)

    def get_all_answers(self):
        # Combine correct answer with incorrect answers
        answers = self.incorrect_answers + [self.correct_answer]
        # Shuffle to randomize the position of the correct answer
        random.shuffle(answers)
        return answers

    @property
    def get_randomized_choices(self):
        """generates a list of answer choices in random order.

        Returns:
            list: A list of answer choices in random order.
        """
        choices = [choice for choice in self.incorrect_answers]
        choices.append(str(self.correct_answer))
        random.shuffle(choices)
        print(choices)
        return choices

class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question)
    time_limit = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class UserResult(models.Model):
    """Represents a user's result for a specific quiz.

    Attributes:
        user (User): The user who took the quiz.
        quiz (Quiz): The quiz that was taken.
        score (int): The user's score for the quiz.
        completion_time (timedelta): The time it took for the user to
        complete the quiz.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    # completion_time = models.DurationField()

    def __str__(self):
        return f"{self.user.username} - " \
               f"{self.quiz.id} - {self.score}"
