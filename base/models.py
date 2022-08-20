from django.db import models
from user.models import Account
from .signals import saveSlug

class Blog(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=400)
    slug = models.SlugField(blank=True,null=True)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='blog/')
    views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['date']
        verbose_name_plural = "Blog"

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_comment = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    class Meta:
        ordering = ['date_comment']
        verbose_name_plural = 'Kommentlar'

    def __str__(self):
        return f'{self.blog.title} - {self.comment}'

class NewsletterFollowers(models.Model):
    email = models.EmailField(unique=True)
    followers = models.ManyToManyField(Account)

    class Meta:
        verbose_name_plural = "Yangiliklar tasmasi obunachilari"

    def __str__(self):
        return self.email

class Contact(models.Model):
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=120, blank=True)
    email = models.EmailField(blank=True)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'Kontakt'

    def __str__(self):
        if not self.user:
            return self.name
        return self.user.username

class Describe(models.Model):
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Maktab haqida ma'lumot"

    def __str__(self):
        return self.text


saveSlug(instance=Blog)