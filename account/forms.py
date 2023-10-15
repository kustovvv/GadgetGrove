from django import forms

from .models import PersonalInformation

import calendar

class FullInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = ['nickname', 'first_name', 'last_name']

        widgets = {
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SettingsImageForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = ['avatar',]

        widgets = {
            'avatar': forms.ClearableFileInput()
        }

class SettingsDateOfBirthForms(forms.Form):
    DAYS = [(str(i), str(i)) for i in range(1, 32)]
    MONTHS = list(enumerate(calendar.month_name[1:]))
    YEARS = list(enumerate(range(2023, 1922, -1)))

    selected_day = forms.ChoiceField(
            choices=[(str(i), str(i)) for i in range(1, 32)],
            widget=forms.Select(attrs={'class': 'form-control'})
        )    
    selected_month = forms.ChoiceField(choices=MONTHS, widget=forms.Select(attrs={'class': 'form-control'}))
    selected_year = forms.ChoiceField(choices=YEARS, widget=forms.Select(attrs={'class': 'form-control'}))

    

class SettingsPhoneForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = ['phone_number',]

        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SettingsSocialProfilesForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = ['facebook', 'instagram', 'twitter', 'google', 'pinterest']

        widgets = {
            'facebook': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control'}),
            'google': forms.TextInput(attrs={'class': 'form-control'}),
            'pinterest': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SettingsAdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = ['about', 'hobby', 'interests']

        widgets = {
            'about': forms.Textarea(attrs={'class': 'form-control'}),
            'hobby': forms.Textarea(attrs={'class': 'form-control'}),
            'interests': forms.Textarea(attrs={'class': 'form-control'}),
        }