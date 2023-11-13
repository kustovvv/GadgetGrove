from item.models import Comments, Item, Category
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('first_name', 'last_name', 'email', 'comment', 'advantages', 'disadvantages')
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}), 
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}), 
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), 
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell us about your purchase'}),
            'advantages': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Advantages'}), 
            'disadvantages': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Disadvantages'}),
        }


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('availability', 'image')

        widgets = {
            'image': forms.ClearableFileInput(),
        }