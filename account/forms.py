from django import forms

from .models import PersonalInformation

import calendar

class FullInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = ['nickname', 
                  'first_name', 
                  'last_name', 
                  'avatar', 
                  'phone_number', 
                  'facebook', 
                  'instagram', 
                  'twitter', 
                  'google', 
                  'pinterest', 
                  'about', 
                  'hobby', 
                  'interests']

        widgets = {
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control'}),
            'google': forms.TextInput(attrs={'class': 'form-control'}),
            'pinterest': forms.TextInput(attrs={'class': 'form-control'}),
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