from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    name = models.CharField(max_length=100)
    
    persons = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField(blank=True)  # optional
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=0)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating}★ - {self.message}"


class LoginLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)  # login / logout etc.
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.timestamp}"
