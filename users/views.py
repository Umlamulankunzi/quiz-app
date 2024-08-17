from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('quiz_list')  # Redirect to a view after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
