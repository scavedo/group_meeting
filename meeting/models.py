from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username


class Project(models.Model):
    name = models.CharField(max_length=128)
    users = models.ManyToManyField(UserProfile)
    completed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Note(models.Model):
    # project = models.ForeignKey('Project')
    # date_added = models.DateTimeField()
    title = models.CharField(max_length=128)
    content = models.TextField()

    def __unicode__(self):
        return self.title


class File(models.Model):
    # project = models.ForeignKey('Project')
    title = models.CharField(max_length=128)
    # date_added = models.DateTimeField()
    file = models.FileField(upload_to='files')

    def __unicode__(self):
        return self.title


class Meeting(models.Model):
    # project = models.ForeignKey('Project')
    # date_added = models.DateTimeField()
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()
    title = models.CharField(max_length=128)
    place = models.CharField(max_length=128)
    description = models.TextField()

    def __unicode__(self):
        return self.title