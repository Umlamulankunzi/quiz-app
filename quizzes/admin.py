from django.contrib import admin
from .models import Category, Question, Quiz


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
        search_fields (tuple): Fields that can be searched using the
            search bar.
        list_filter (tuple): Fields by which the list can be filtered.
    """
    list_display = ('question_text', 'question_type', 'category', 'difficulty')
    search_fields = ('question_text', )
    list_filter = ('is_approved', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


# @admin.register(UserResult)
# class UserResultAdmin(admin.ModelAdmin):
#     list_display = ('user', 'quiz', 'score')
