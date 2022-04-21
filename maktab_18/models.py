from django.db import models
from cloudinary.models import CloudinaryField

class Home(models.Model):
    name = models.CharField('Ism',max_length=150)
    phone_number = models.CharField('Telefon raqam',max_length=13)
    email = models.EmailField('Elektron Pochta', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Kurslarga yozilish'

class Member(models.Model):
    email = models.EmailField('Email')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Obunalar'

class Text(models.Model):
    text = models.TextField('Matn')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = "Ma'lumot"

class Element(models.Model):
    name = models.CharField('Ism',max_length=30)
    sourname = models.CharField('Familiya',max_length=50)
    email = models.EmailField('Elektron Pochta')
    address = models.CharField('Manzil',max_length=150)
    phone_number = models.CharField('Telefon Raqam',max_length=13)
    message = models.TextField('Xabar')

    def __str__(self):
        return self.name + '' + self.sourname

    class Meta:
        verbose_name_plural = 'Arizalar'

class Lesson(models.Model):
    subject = models.CharField('Fan',max_length=50)
    cost = models.CharField('Narx',max_length=50)
    teacher_name = models.CharField("O'qituvchi ismi",max_length=200)
    in_week = models.IntegerField('Haftada')
    time = models.CharField("Vaqt oralig'",max_length=13)
    description = models.CharField('Tasvir',max_length=90)
    views = models.PositiveIntegerField("Ko'rishlar soni", default=0)
    image = CloudinaryField()


    def __str__(self):
        return self.subject

    class Meta:
        verbose_name_plural = 'Kurslar'

class Author(models.Model):
    author_name = models.CharField('Ism',max_length=150)
    meta = models.URLField('Meta')
    twitter = models.URLField('Twitter')
    instagram = models.URLField('Instagram')
    telegram = models.URLField('Telegram')
    about_author = models.TextField('Muallif haqida')

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name_plural = 'Muallif'

class Blog(models.Model):
    title = models.CharField('Sarlavha',max_length=200)
    text = models.TextField('Matn')
    date = models.DateField('Sana')
    image = CloudinaryField()

    def __str__(self):
        return self.title

    def get_comments(self):
        return self.comment_set.all()

    class Meta:
        verbose_name_plural = 'Blog'

class Contact(models.Model):
    name = models.CharField('Ism',max_length=150)
    email = models.EmailField('Elektron Pochta')
    theme = models.CharField('Mavzu',max_length=200, null=True, blank=True)
    message = models.TextField('Xabar matni')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Kontakt'

class Comment(models.Model):
    choose = models.ForeignKey(Blog, on_delete=models.CASCADE, editable=True)
    name = models.CharField('Ism',max_length=150, null=True, blank=True, editable=True)
    email = models.EmailField('Elektron Pochta',null=True, blank=True, editable=True)
    date_comment = models.DateField('Sana', null=True, blank=True, editable=True, auto_now_add=True)
    comment = models.TextField('Izoh',null=True, blank=True, editable=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Izohlar'

class Feedback(models.Model):
    course = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['course',]
        verbose_name_plural = "Fikrlar"

class ExamQuestion(models.Model):
    name = models.CharField(max_length=100)
    exam_file = CloudinaryField()
    photo = CloudinaryField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    exam_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Imtixon savollari portali"

class TheBestPupils(models.Model):
    pupil_name = models.CharField(max_length=150)
    about_pupil = models.TextField(max_length=700)
    pupil_photo = CloudinaryField()
    start_study_years = models.DateField()
    end_study_years = models.DateField()
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.pupil_name

    class Meta:
        verbose_name_plural = "Eng yaxshi o'quvchilar"