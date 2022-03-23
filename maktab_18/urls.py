from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    path('course-details/<lesson_id>',views.lessons, name='lessons'),
    path('about/',views.about,name='about'),
    path('search/',views.search, name='search'),
    path('courses/',views.courses,name='courses'),
    path('ariza-topshirish/',views.elements,name='elements'),
    path('blog/',views.blog,name='blog'),
    path('blog/details/<int:pk>',views.blogdetails, name='blog-single'),
    path('author/<author_id>',views.author, name='author'),
    path('contacts/',views.contacts,name='contacts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)