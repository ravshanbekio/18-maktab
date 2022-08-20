from django.contrib import admin
from course.models import Course,Teacher, Feedback

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Feedback)