from django.contrib import admin
from .models import Announcement,Enroll_Data,RegisteredStudents,Student
admin.site.register(Announcement)
admin.site.register(RegisteredStudents)
admin.site.register(Enroll_Data)
admin.site.register(Student)

# Register your models here.
