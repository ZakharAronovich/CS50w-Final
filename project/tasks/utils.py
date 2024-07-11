from .models import Announcement, Course


def announce_task(course_id):
    course = Course.objects.get(pk=course_id)
    text = f"{course.teacher.user.name} created a new task for {course.title} course."
    
    Announcement.objects.create(course=course, text=text)