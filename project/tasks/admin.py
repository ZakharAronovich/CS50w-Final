from django.contrib import admin
from .models import User, Teacher, Student, Task, Group


admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Task)
admin.site.register(Group)
