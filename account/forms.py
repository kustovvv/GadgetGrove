from django import forms

from .models import PersonalInformation
from authentication.models import User

import calendar

class InfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 
                  'first_name', 
                  'last_name',
                  ]
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            }


class FullInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = ['avatar_url', 
                  'phone_number', 
                  'facebook_url', 
                  'instagram_url', 
                  'twitter_url', 
                  'google_url', 
                  'pinterest_url', 
                  'about', 
                  'hobby', 
                  'interests']

        widgets = {
            'avatar_url': forms.ClearableFileInput(),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'google_url': forms.TextInput(attrs={'class': 'form-control'}),
            'pinterest_url': forms.TextInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),
            'hobby': forms.Textarea(attrs={'class': 'form-control'}),
            'interests': forms.Textarea(attrs={'class': 'form-control'}),
        }

class SettingsDateOfBirthForms(forms.Form):
    DAYS = list(enumerate(range(1, 32)))
    MONTHS = list(enumerate(calendar.month_name[1:]))
    YEARS = list(enumerate(range(2023, 1922, -1)))

    selected_day = forms.ChoiceField(choices=DAYS, widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    selected_month = forms.ChoiceField(choices=MONTHS, widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    selected_year = forms.ChoiceField(choices=YEARS, widget=forms.Select(attrs={'class': 'form-control'}), required=False)