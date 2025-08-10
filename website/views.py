from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Booking, Feedback, LoginLog
from .forms import FeedbackForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone


# =======================
# Public Pages
# =======================
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def contact(request):
    return render(request, 'contact.html')

def login_page(request):
    return render(request, 'login.html')

def service(request):
    return render(request, 'service.html')


# =======================
# User Registration
# =======================
def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return HttpResponse("❌ Passwords do not match.")

        if User.objects.filter(username=username).exists():
            return HttpResponse("❌ Username already exists.")

        User.objects.create_user(username=username, password=password)
        return HttpResponse("✅ Account created successfully. Please log in.")
    
    return redirect('login')


# =======================
# User Login
# =======================
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

            # ✅ Login log save
            LoginLog.objects.create(
                user=user,
                action="login",
                timestamp=timezone.now()
            )

            return redirect('home')
        else:
            return HttpResponse("❌ Invalid username or password.")

    return redirect('login')


# =======================
# User Logout
# =======================
def logout_user(request):
    if request.user.is_authenticated:
        # ✅ Logout log save
        LoginLog.objects.create(
            user=request.user,
            action="logout",
            timestamp=timezone.now()
        )

    logout(request)
    return redirect('login')


# =======================
# Book Table
# =======================
@login_required(login_url='login')
def book_table(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        persons = request.POST.get('persons')
        date = request.POST.get('date')
        time = request.POST.get('time')

        Booking.objects.create(
            name=name,
            persons=persons,
            date=date,
            time=time
        )

        return HttpResponse("✅ Booking Saved! Thank you.")

    return render(request, 'book.html')


# =======================
# Feedback View
# =======================
@login_required(login_url='login')
def feedback_view(request):
    feedbacks = Feedback.objects.all().order_by('-timestamp')

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.rating = request.POST.get('rating')  # ⭐ Star rating save
            feedback.save()
            return redirect('feedback')
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {
        'form': form,
        'feedbacks': feedbacks
    })
