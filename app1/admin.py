from django.contrib import admin
from django.contrib.admin.models import LogEntry
from . models import *
# Register your models here.

LogEntry._meta.get_field('user').remote_field.model = User1

admin.site.register(User1)
admin.site.register(Complaintboarder)
admin.site.register(Complaintcyber)
admin.site.register(Complaintterror)