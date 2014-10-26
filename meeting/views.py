from django.shortcuts import render, render_to_response
from django.template import RequestContext
from meeting.forms import UserForm, UserProfileForm, ProjectForm, NotesForm, FilesForm, MeetingForm, AddUserForm
from meeting.models import UserProfile, Project, Note, Meeting, File
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from itertools import chain


# Create your views here.
@login_required(login_url='/login/')
def index(request):
    user = UserProfile.objects.get(user=request.user)
    projects = user.project_set.all()
    active_projects = projects.filter(completed=False)
    completed_projects = projects.filter(completed=True)
    pid = request.GET.get('pid')
    request.session['pid'] = pid
    if pid:
        display_project = projects.filter(id=pid)
    else:
        display_project = None
    return render(request, 'meeting/index.html', {
        'projects': projects,
        'active_projects': active_projects,
        'completed_projects': completed_projects,
        'display_project': display_project
    })


def about(request):
    return render(request, 'meeting/about.html')


def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response('meeting/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }, context)


def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('meeting/login.html', {}, context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/login/')
def create_project(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = UserProfile.objects.get(user=request.user)
            project.save()
            project.users.add(UserProfile.objects.get(user=request.user))
            project.save()
            return HttpResponseRedirect('/')
        else:
            print form.errors
    else:
        form = ProjectForm()
    return render_to_response('meeting/create-project.html', {'form': form}, context)


@login_required(login_url='/login/')
def add_user(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            pid = request.session.get('pid')
            if not pid:
                messages.add_message(request, messages.WARNING, 'You need to select a project before you can add a user.')
                return HttpResponseRedirect('/')
            else:
                project = Project.objects.get(id=pid)
                this = form.cleaned_data['user']
                if User.objects.filter(username=this):
                    user = User.objects.filter(username=this)
                else:
                    print "invalid username"
                project.users.add(UserProfile.objects.get(user=user))
                project.save()
                return HttpResponseRedirect('/')

        else:
            print form.errors
    else:
        form = AddUserForm()
    return render_to_response('meeting/add-user.html', {'form': form}, context)


@login_required(login_url='/login/')
def add_meeting(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            pid = request.session.get('pid')
            if not pid:
                messages.add_message(request, messages.WARNING, 'You need to select a project before you can add a meeting.')
                return HttpResponseRedirect('/')
            else:
                meeting = form.save(commit=False)
                meeting.project = Project.objects.get(id=pid)
                meeting.save()
                return HttpResponseRedirect('/')
        else:
            print form.errors
    else:
        form = MeetingForm()
    return render_to_response('meeting/add-meeting.html', {'form': form}, context)


@login_required(login_url='/login/')
def add_file(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            pid = request.session.get('pid')
            if not pid:
                messages.add_message(request, messages.WARNING, 'You need to select a project before you can add a file.')
                return HttpResponseRedirect('/')
            else:
                fileform = form.save(commit=False)
                fileform.project = Project.objects.get(id=pid)
                if 'file' in request.FILES:
                    fileform.file = request.FILES['file']
                else:
                    print "no"
                fileform.save()
                return HttpResponseRedirect('/')
        else:
            print form.errors
    else:
        form = FilesForm()
    return render_to_response('meeting/add-file.html', {'form': form}, context)


@login_required(login_url='/login/')
def add_note(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            pid = request.session.get('pid')
            if not pid:
                messages.add_message(request, messages.WARNING, 'You need to select a project before you can add a note.')
                return HttpResponseRedirect('/')
            else:
                note = form.save(commit=False)
                note.project = Project.objects.get(id=pid)
                note.save()
                return HttpResponseRedirect('/')
        else:
            print form.errors
    else:
        form = NotesForm()
    return render_to_response('meeting/add-note.html', {'form': form}, context)


def calendar(request):
    pid = request.GET.get('pid')
    if pid:
        meetings = Meeting.objects.filter(project=pid)
    else:
        print "no"
        meetings = None
    return render(request, 'meeting/calendar.html', {
        'meetings': meetings,
    })


def notes(request):
    pid = request.GET.get('pid')
    if pid:
        notes = Note.objects.filter(project=pid)
    else:
        print "no"
        notes = None
    return render(request, 'meeting/notes.html', {
        'notes': notes,
    })


def files(request):
    pid = request.GET.get('pid')
    if pid:
        files = File.objects.filter(project=pid)
    else:
        print "no"
        files = None
    return render(request, 'meeting/files.html', {
        'files': files,
    })


def home(request):
    pid = request.GET.get('pid')
    if pid:
        files = File.objects.filter(project=pid)
        meetings = Meeting.objects.filter(project=pid)
        notes = Note.objects.filter(project=pid)
        added = sorted(list(chain(files, meetings, notes)), key=lambda instance: instance.date_added)
    else:
        print "no"
        files = None
    return render(request, 'meeting/project-home.html', {
        'added': added,
    })