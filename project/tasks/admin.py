from django.contrib import admin
from .models import User, Teacher, Student, Task, Course, Tag, Notification, Review


admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Task)
admin.site.register(Course)
admin.site.register(Tag)
admin.site.register(Notification)
admin.site.register(Review)