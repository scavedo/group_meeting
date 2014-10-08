from django.contrib import admin
from meeting.models import UserProfile, Project, Note, File, Meeting


# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ['name', 'notes', 'files', 'calendar', 'completed']


admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Note)
admin.site.register(File)
admin.site.register(Meeting)
