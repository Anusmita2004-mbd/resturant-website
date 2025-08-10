from django.contrib import admin
from django.utils.html import format_html
from .models import Booking, Feedback, LoginLog

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rating_stars', 'message', 'timestamp')
    list_filter = ('rating', 'timestamp')
    search_fields = ('name', 'email', 'message')

    def rating_stars(self, obj):
        full_star = '<span style="color:gold;">&#9733;</span>'  # হলুদ স্টার
        empty_star = '<span style="color:lightgray;">&#9733;</span>'  # ধূসর স্টার
        return format_html(full_star * obj.rating + empty_star * (5 - obj.rating))
    
    rating_stars.short_description = 'Rating'

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'persons', 'date', 'time')
    list_filter = ('date', 'time')
    search_fields = ('name',)

@admin.register(LoginLog)
class LoginLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'action')
    list_filter = ('action', 'timestamp')
    search_fields = ('user__username',)
