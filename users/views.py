from django.shortcuts import render, redirect
from django.contrib.auth import login, views as auth_views
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to a view after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


class CustomLoginView(auth_views.LoginView):
    """Custom login view class that more functionality to default view

    Redirects user to quiz_list when loggen in user tries to navigate to
    login url. Class inherits from django LoginView
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('category_list')
        return super().dispatch(request, *args, **kwargs)
