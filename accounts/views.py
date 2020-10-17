from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object
            new_user = user_form.save(commit=False)

            # Set the chosen password
            # Password encryption
            new_user.set_password(user_form.cleaned_data['password'])

            # Save the new user
            new_user.save()

            return render(request, 'accounts/register_done.html', {'new_user':new_user})
    
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'user_form':user_form})


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('passwordsapp:home')
                else:
                    messages.error(request, "Disabled account")

            else:
                messages.error(request, "Invalid login attempt")
            
    else:
        login_form = LoginForm()
    return render(request, 'accounts/login.html', {'login_form':login_form})