from meeting.models import UserProfile, Project
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.EmailField(help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(help_text="Select a profile image to upload.", required=False)

    class Meta:
        model = UserProfile
        fields = ['picture']


class ProjectForm(forms.ModelForm):
    name = forms.CharField(help_text="Please enter a project name.")
    # users = forms.MultipleChoiceField(widget=forms.HiddenInput())
    # notes = forms.BooleanField(help_text="Include Notes.", initial=True)
    # files = forms.BooleanField(help_text="Include Files.", initial=True)
    # calendar = forms.BooleanField(help_text="Include a Calendar.", initial=True)

    class Meta:
        model = Project
        # fields = ['name', 'notes', 'files', 'calendar']
        fields = ['name']
