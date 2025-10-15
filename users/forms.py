from django.forms import ModelForm
from django import forms
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exlude = ['user']
        labels = {
            'realname':'name'
        }
        widgets={
            'image':forms.FileInput(),
            'bio':forms.Textarea(attrs={'rows':3})
        }