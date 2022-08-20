from django.urls import path
from .views import (HomeView, AboutView, AddToSchoolView,
                    BlogView, BlogDetailView, ContactView,
                    SearchBlogView )

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('about/',AboutView.as_view(), name='about'),
    path('add-school/',AddToSchoolView.as_view(), name='add-to-school'),
    path('blog/',BlogView.as_view(), name='blog'),
    path('blog/<date>/<slug:slug>/',BlogDetailView.as_view(), name='blog-detail'),
    path('contact/',ContactView.as_view(), name='contact'),
    path('search/blog/',SearchBlogView.as_view(), name='search-blogs'),
]