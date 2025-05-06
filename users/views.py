from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "تم التسجيل بنجاح.")
            return redirect('login')  
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    form = UserLoginForm(data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, "تم تسجيل الدخول بنجاح.")
        return redirect('index') 
    return render(request, 'users/login.html', {'form': form})

@login_required
def index(request):
    return render(request, 'users/index.html')

def logout_view(request):
    logout(request)
    messages.success(request, "لقد قمت بتسجيل الخروج بنجاح.")
    return redirect('index')