from meeting.models import UserProfile, Project, Note, File, Meeting, Action
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
    due_date = forms.DateTimeField(widget=forms.DateTimeInput(format='%m/%d/%Y %H:%M %p'), input_formats=['%m/%d/%Y %H:%M %p'], localize=True)

    class Meta:
        model = Project
        fields = ['name', 'due_date']


class NotesForm(forms.ModelForm):
    title = forms.CharField(help_text="Please enter the title of your note.")
    content = forms.Textarea()

    class Meta:
        model = Note
        fields = ['title', 'content']


class FilesForm(forms.ModelForm):
    title = forms.CharField(help_text="Please enter a title for your file.")
    file = forms.FileField(help_text="Upload your file.")

    class Meta:
        model = File
        fields = ['title', 'file']


class MeetingForm(forms.ModelForm):
    title = forms.CharField(help_text="Please enter a title for your meeting.")
    date_begin = forms.DateTimeField(widget=forms.DateTimeInput(format='%m/%d/%Y %H:%M %p'), input_formats=['%m/%d/%Y %H:%M %p'], localize=True)
    date_end = forms.DateTimeField(widget=forms.DateTimeInput(format='%m/%d/%Y %H:%M %p'), input_formats=['%m/%d/%Y %H:%M %p'], localize=True)
    place = forms.CharField(help_text="Enter the location.")
    description = forms.Textarea()

    class Meta:
        model = Meeting
        fields = ['title', 'date_begin', 'date_end', 'place', 'description']


class AddUserForm(forms.ModelForm):
    user = forms.CharField()

    class Meta:
        model = Project
        fields = ['user']


class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = []


class DeleteNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = []


class DeleteFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = []


class DeleteMeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = []


class FinishProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = []


class DeleteProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = []