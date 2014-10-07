from django.contrib import admin
from meeting.models import UserProfile, Project, Notes, Files, Calendar


# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ['name', 'notes', 'files', 'calendar', 'completed']


admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Notes)
admin.site.register(Files)
admin.site.register(Calendar)
