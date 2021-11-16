from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.fields import Field
from main.models import ReadingStatus, ReadingProgress
from .models import Profile

class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'name':'username',
            'id':'username',
            'required':'',
            'type': 'text',
            'class': 'form-login',
            'maxlength':'16',
            'minlength':'3',
            'placeholder':'Username',
            'autocomplete':'off'
            })
        self.fields["email"].widget.attrs.update({
            'name':'email',
            'id':'email',
            'required':'',
            'type': 'email',
            'class': 'form-login',
            'placeholder':'E-mail',
            'autocomplete':'off'
            })
        self.fields["password1"].widget.attrs.update({
            'name':'password1',
            'id':'password1',
            'required':'',
            'type': 'password',
            'class': 'form-login',
            'maxlength':'22',
            'minlength':'6',
            'placeholder':'Password',
            'autocomplete':'off'
            })
        self.fields["password2"].widget.attrs.update({
            'name':'password2',
            'id':'password2',
            'required':'',
            'type': 'password',
            'class': 'form-login',
            'maxlength':'22',
            'minlength':'6',
            'placeholder':'Password',
            'autocomplete':'off'
            })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class BookAddingForm(forms.ModelForm):
    google_id = forms.CharField(max_length=30, widget=forms.HiddenInput())
    title = forms.CharField(widget=forms.HiddenInput(), required=False)
    description = forms.CharField(widget=forms.HiddenInput(), required=False)
    cover_url = forms.CharField(widget=forms.HiddenInput(), required=False)
    authors = forms.CharField(widget=forms.HiddenInput(), required=False)
    info_url = forms.CharField(widget=forms.HiddenInput())
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["list_type_add"].widget.attrs.update({
            'name':'list_type',
            'required':'',
            'class': 'option-list',
            })

    class Meta:
        model = ReadingStatus
        fields = ['list_type']

class ListUpdateForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["list_type"].widget.attrs.update({
            'name':'list_type_update',
            'required':'',
            'class': 'option-list',
            })

    class Meta:
        model = ReadingStatus
        fields = ['list_type']


class ProgressUpdate(forms.ModelForm):
    
    class Meta:
        model = ReadingProgress
        fields = ['year_goal']
