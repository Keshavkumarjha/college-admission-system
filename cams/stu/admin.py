from django.contrib import admin
from.models import Student,Student_status




@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # ...
    list_display = ('studentname','coursename','fathername','mothername','emall','gender','category','dob','mono','village','distic','state','pincode','boardname','tenmarks','twboard','twmarks','university','graduation')




@admin.register(Student_status)
class StudentstatusAdmin(admin.ModelAdmin):
    list_display = ('status','reason')


