from django import forms
from .models import Feedback, Booking

class FeedbackForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'rating', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'date', 'time', 'persons']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
