from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from meeting.forms import UserForm, UserProfileForm, ProjectForm, NotesForm, FilesForm, MeetingForm
from meeting.models import UserProfile, Project
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login/')
def index(request):
    user = UserProfile.objects.get(user=request.user)
    projects = user.project_set.all()
    active_projects = user.project_set.filter(completed=False)
    completed_projects = user.project_set.filter(completed=True)
    return render(request, 'meeting/index.html', {
        'projects': projects,
        'active_projects': active_projects,
        'completed_projects': completed_projects
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

    return render_to_response(
            'meeting/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)


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


def add_meeting(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print form.errors
    else:
        form = MeetingForm()
    return render_to_response('meeting/add-meeting.html', {'form': form}, context)


def add_file(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = FilesForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print form.errors
    else:
        form = FilesForm()
    return render_to_response('meeting/add-file.html', {'form': form}, context)


def add_note(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print form.errors
    else:
        form = NotesForm()
    return render_to_response('meeting/add-note.html', {'form': form}, context)
