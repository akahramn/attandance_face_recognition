from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        print("USER=", user.get_full_name())
        return redirect('http://127.0.0.1:8000/attendance/1/home-page')
    return render(request, 'accounts/form.html', {'form': form})


def logout_view(request):
    logout(request)

    return redirect('http://127.0.0.1:8000/accounts/login')
