from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm, LoginForm


def signup_view(request):
    """
    GET  → Show empty signup form
    POST → Validate form → Create user → Auto-login → Redirect to home
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to BabyBloom, {user.username}! 🎉')
            return redirect('home')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = SignupForm()

    return render(request, 'users/signup.html', {'form': form})


def login_view(request):
    """
    GET  → Show login form
    POST → Authenticate → Login → Redirect to next or home
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}! 👋')
                # Redirect to 'next' URL if present (e.g. when @login_required redirects here)
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please fill in all fields.')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    """
    GET → Logout user → Redirect to login page
    """
    logout(request)
    messages.info(request, 'You have been logged out. See you soon! 👋')
    return redirect('login')
