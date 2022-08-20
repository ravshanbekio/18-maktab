from django.db import models
from user.models import Account
from .signals import saveCourseSlug

class Course(models.Model):
    course_name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True,null=True)
    course_teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    course_description = models.TextField(max_length=700)
    course_cost = models.PositiveIntegerField(default=0)
    in_week = models.PositiveIntegerField(default=2)
    time = models.CharField(max_length=13)
    views = models.PositiveIntegerField(default=0)
    course_photo = models.ImageField(upload_to='course-image/') 
    students_list = models.ManyToManyField(Account, blank=True)

    class Meta:
        verbose_name_plural = "Kurslar"

    def __str__(self):
        return self.course_name

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=120)
    teacher_direction = models.CharField(verbose_name="O'qituvchi yo'nalishi",max_length=50)

    class Meta:
        ordering = ['teacher_name']
        verbose_name_plural = "O'qituvchilar haqida ma'lumot"

    def __str__(self):
        return f'{self.teacher_name} - {self.teacher_direction}'


class Feedback(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='get_course_users')
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Feedback'

    def __str__(self):
        return f'{self.course.course_name} - {self.message}'

saveCourseSlug(instance=Course)