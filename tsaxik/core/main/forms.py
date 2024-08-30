from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile,SupportMessage

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Օգտ․ անուն', max_length=64)
    password = forms.CharField(label='Գաղտնաբառ', widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']

class SupportForm(forms.ModelForm):
    subject = forms.CharField(label='Թեմա', max_length=100)
    message = forms.CharField(label='Հաղորդագրություն', widget=forms.Textarea)

    class Meta:
        model = SupportMessage
        fields = ['subject', 'message']