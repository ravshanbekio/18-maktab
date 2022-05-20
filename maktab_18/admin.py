from django.contrib import admin
from .models import Home, Member, Text, Element, Lesson, Blog, Contact, Author, Comment, Feedback, ExamQuestion, TheBestPupils

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    fields = ('name','phone_number','email')
    list_display = ('name','phone_number','email')
    list_filter = ('name','phone_number')
    ordering = ['name']
    search_fields = ['name','email']

admin.site.register(Member)
admin.site.register(Text)

@admin.register(Element)
class ElementsAdmin(admin.ModelAdmin):
    fields = ('name','sourname','email','address','phone_number','message')
    list_display = ('name','sourname','phone_number')
    list_filter = ('name','sourname','address','phone_number')
    ordering = ['name','sourname']
    search_fields = ['name','sourname','phone_number']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    fields = ('subject','cost','teacher_name','in_week','time','description','image')
    list_display = ('subject','cost')
    list_filter = ('subject','cost')
    ordering = ['subject']
    search_fields = ['subject','cost','description']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ('name','email','theme','message')
    list_display = ('id','name','email')
    search_fields = ['name','email']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('author_name','meta','twitter','instagram','telegram','about_author')
    list_display = ('author_name','telegram')
    search_fields = ['name']
 

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Feedback)
admin.site.register(ExamQuestion)
admin.site.register(TheBestPupils)