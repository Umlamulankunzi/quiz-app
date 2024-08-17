from django.contrib import admin
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Admin interface config for CustomUser model.

    This class customizes the admin interface for managing user
    objects in the Django admin site.

    Attributes:
        list_display (tuple): Fields to be displayed in the list view.
            In this case, 'username' and 'is_quiz_master'.
        search_fields (tuple): Fields that can be searched using the
            search bar. In this case, 'username'.
    """
    list_display = ('username', 'is_quiz_master')
    search_fields = ('username',)
