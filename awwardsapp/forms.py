from django import forms
from django.forms.widgets import Textarea
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_pic','contact']
        widgets = {
            'bio': Textarea(attrs={'cols': 30, 'rows': 3}),
        }
