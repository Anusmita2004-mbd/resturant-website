from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),                 # Default route → login page
    path('home/', views.index, name='home'),                  # ✅ Changed name='index' → name='home'
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),


    # Protected routes
    path('book/', views.book_table, name='book'),             # Only for logged-in users
    path('feedback/', views.feedback_view, name='feedback'),  # Only for logged-in users

    # Auth system
    path('login/', views.login_page, name='login'),           # Login form page
    path('login_user/', views.login_user, name='login_user'),         # POST request login
    path('register_user/', views.register_user, name='register_user'), # POST request register
    path('logout/', views.logout_user, name='logout'),        # Logout route
]
