from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegister
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        user_form = UserRegister(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        user_form = UserRegister()
    return render(request, 'users/register.html', {'user_form': user_form})


@login_required
def profile(request):
    return render(request, 'user/profile.html')
