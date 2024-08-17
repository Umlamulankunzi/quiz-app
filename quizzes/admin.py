from django.contrib import admin
from .models import Category, Quiz, Question, UserResult


# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Admin interface config for Question model.

    This class customizes the admin interface for managing Question
    objects in the Django admin site. It specifies which fields are
    displayed in the list view, allows searching by certain fields,
    and adds filtering options based on related fields.

    Attributes:
        list_display (tuple): Fields to be displayed in the list view.
            In this case, 'text', 'correct_answer', and 'quiz'.
        search_fields (tuple): Fields that can be searched using the
            search bar. In this case, 'text' and 'correct_answer'.
        list_filter (tuple): Fields by which the list can be filtered.
            In this case, 'quiz' to filter questions by associated quiz.
    """
    list_display = ('text', 'correct_answer', 'quiz')
    search_fields = ('text', 'correct_answer')
    list_filter = ('quiz',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_by', 'approved')
    list_filter = ('category', 'approved')
    search_fields = ('title', 'description')


@admin.register(UserResult)
class UserResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'completion_time')
