from django.urls import path
from .views import CourseView, CourseDetailView, AddStudentToCourseView, SearchCourseView

urlpatterns = [
    path('all',CourseView.as_view(), name='courses'),
    path('<slug:slug>/',CourseDetailView.as_view(), name='course-detail'),
    path('add/<slug:slug>/',AddStudentToCourseView.as_view(), name='add-student'),
    path('search/course/',SearchCourseView.as_view(), name='search-course'),
]