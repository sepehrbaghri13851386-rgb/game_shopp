from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login_app/login.html', {'error': 'ایمیل یا رمز عبور اشتباه است'})

    return render(request, 'login_app/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'login_app/register.html', {'error': 'رمزهای عبور مطابقت ندارند'})

        if User.objects.filter(username=username).exists():
            return render(request, 'login_app/register.html', {'error': 'این نام کاربری قبلا ثبت شده است'})

        if User.objects.filter(email=email).exists():
            return render(request, 'login_app/register.html', {'error': 'این ایمیل قبلا ثبت شده است'})

        user = User.objects.create_user(username=username, email=email, password=password1)
        Profile.objects.create(user=user)
        auth_login(request, user)
        return redirect('home')

    return render(request, 'login_app/register.html')


@login_required
def home_view(request):
    return render(request, 'login_app/home.html')

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        if request.FILES.get("avatar"):
            profile.avatar = request.FILES["avatar"]
            profile.save()
        return redirect('profile')

    return render(request, "login_app/profile.html", {"profile": profile})


def logout_view(request):
    auth_logout(request)
    return redirect('login')