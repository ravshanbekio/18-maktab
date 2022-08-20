from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .models import Course
from .forms import FeedbackForm
from .utils import searchCourse

class SearchCourseView(View):
    def get(self, request):

        search_query, courses = searchCourse(request)

        return render(request, 'search_course.html', {'search_query':search_query, 'courses':courses})

class CourseView(View):
    def get(self, request):

        get_courses = Course.objects.all()[:6]

        context = {
            'courses':get_courses
        }

        return render(request, 'courses/courses.html', context)

class CourseDetailView(View):
    def get(self, request, slug):
        
        get_course = Course.objects.get(slug=slug)
        get_course.views += 1
        get_course.save()

        context = {
            'course':get_course,
            'form':FeedbackForm
        }

        return render(request, 'courses/course-details.html', context)

    def post(self, request, slug):

        get_course = Course.objects.get(slug=slug)

        form = FeedbackForm(request.POST or None)
        if form.is_valid():
            feedback = form.save(commit=False)
            for students in get_course.students_list.all():
                if request.user == students:
                    feedback.course = get_course
                    feedback.user = request.user
                    feedback.save()
                    messages.success(request, "Feedback qoldirildi")
                    return redirect('course-detail',slug=slug)
                else:
                    messages.error(request, "Siz ushbu kursga yozilmagansiz. Iltimos, avval kursga yoziling!")
                    return redirect('course-detail',slug=slug)

class AddStudentToCourseView(View):
    def get(self, request, slug):
        if request.user.is_authenticated:

            get_course = Course.objects.get(slug=slug)

            get_course.students_list.add(request.user)
            get_course.save()
        else:
            return redirect('login')

        return redirect('course-detail',slug=slug)