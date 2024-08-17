from django.db import models
from django.conf import settings


# Create your models here.


class Category(models.Model):
    """Represents a category for organizing quizzes.

    Attributes:
        name (str): The name of the category. Must be unique and can
        have a maximum length of 150 characters.
    """
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return str(self.name)


class Quiz(models.Model):
    """Represents a quiz, which belongs to a category

    Attributes:
        title (str): The title of the quiz. Max length 200 characters.
        description (str): A brief description of the quiz.
        category (Category): The category to which this quiz belongs.
        created_by (User): The user who created the quiz.
        approved (bool): Indicates whether the quiz has been approved
        by an admin. Default is False.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)

class Question(models.Model):
    """Represents a question within a quiz.

    Attributes:
        quiz (Quiz): The quiz to which this question belongs.
        text (str): The text of the question. Max length of 255 characters.
        correct_answer (str): The correct answer for the question.
        choices (list): A JSON field that stores the possible answer
        choices as a dict with key-value pair.
    """
    quiz = models.ForeignKey(
        Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    choices = models.JSONField()

    def __str__(self):
        return str(self.text)

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
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    # completion_time = models.DurationField()

    def __str__(self):
        return f"{self.user.username} - " \
               f"{self.quiz.title} - {self.score}"
