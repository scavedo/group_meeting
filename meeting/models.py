from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


DEFAULT_USER_ID = 1
DEFAULT_PROJECT_ID = 1


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username


class Project(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(UserProfile, related_name="proj_owner")
    users = models.ManyToManyField(UserProfile)
    due_date = models.DateTimeField(blank=True, null=False)
    completed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def is_past_due(self):
        if date.today() > self.due_date:
            return True
        return False


class Note(models.Model):
    project = models.ForeignKey('Project', default=DEFAULT_PROJECT_ID)
    date_added = models.DateTimeField(default=datetime.now())
    added_by = models.ForeignKey('UserProfile', default=DEFAULT_USER_ID)
    title = models.CharField(max_length=128)
    content = models.TextField()

    def __unicode__(self):
        return self.title


def file_path(instance, filename):
    return '/'.join(['files', str(instance.project.name.replace(" ", "_")), filename])


class File(models.Model):
    project = models.ForeignKey('Project', default=DEFAULT_PROJECT_ID)
    date_added = models.DateTimeField(default=datetime.now())
    added_by = models.ForeignKey('UserProfile', default=DEFAULT_USER_ID)
    title = models.CharField(max_length=128)
    file = models.FileField(upload_to=file_path)

    def __unicode__(self):
        return self.title


class Meeting(models.Model):
    project = models.ForeignKey('Project', default=DEFAULT_PROJECT_ID)
    date_added = models.DateTimeField(default=datetime.now())
    added_by = models.ForeignKey('UserProfile', default=DEFAULT_USER_ID)
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()
    title = models.CharField(max_length=128)
    place = models.CharField(max_length=128)
    description = models.TextField()

    def __unicode__(self):
        return self.title

    def begin_format(self):
        return '%s' % self.date_begin.strftime('%Y-%m-%dT%H:%M:%S')

    def end_format(self):
        return '%s' % self.date_end.strftime('%Y-%m-%dT%H:%M:%S')