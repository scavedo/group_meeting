from meeting.models import UserProfile


def base(request):
    user = UserProfile.objects.get(user=request.user)
    projects = user.project_set.all()
    active_projects = projects.filter(completed=False)
    completed_projects = projects.filter(completed=True)
    return {
        'projects': projects,
        'active_projects': active_projects,
        'completed_projects': completed_projects
    }