from django.db.models import Q
from .models import Course

def searchCourse(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    courses = Course.objects.filter(
        Q(course_name__icontains=search_query)|
        Q(course_teacher__teacher_name__icontains=search_query)|
        Q(course_cost__icontains=search_query)|
        Q(course_description__icontains=search_query)
    )

    return search_query, courses
    