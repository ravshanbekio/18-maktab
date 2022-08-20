from django.db.models import Q
from .models import Blog

def searchBlog(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    blogs = Blog.objects.filter(
            Q(title__icontains=search_query)|
            Q(subtitle__icontains=search_query)|
            Q(body__icontains=search_query)
        )

    return search_query, blogs