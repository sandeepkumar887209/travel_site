from django import forms
from .models import TravelQuery
from .models import Review

class TravelQueryForm(forms.ModelForm):
    class Meta:
        model = TravelQuery
        fields = ['name', 'email', 'whatsapp_number', 'destination', 'travel_date']
        widgets = {
            'travel_date': forms.DateInput(attrs={'type': 'date'}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'rating', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
