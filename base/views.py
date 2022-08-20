from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.db.models import Q
from course.models import Course
from .models import Blog, Describe, Comment
from .forms import CommentForm, AuthenticatedUserContactForm, AnonymousUserContactForm
from .utils import searchBlog

class SearchBlogView(View):
    def get(self, request):

        search_query, blogs = searchBlog(request)

        return render(request, 'search_blog.html',{'search_query':search_query, 'blogs':blogs})

class SearchView(View):
    def get(self, request):
        return render(request, 'search.html')

class HomeView(View):
    def get(self, request):

        preview_courses = Course.objects.all()[:6]
        blogs = Blog.objects.all()[:3]

        context = {
            'courses':preview_courses,
            'blogs':blogs
        }

        return render(request, 'main/index.html', context)

class AboutView(View):
    def get(self, request):

        description_school = Describe.objects.all()[:1]

        context = {
            'texts':description_school
        }

        return render(request, 'main/about.html', context)

class AddToSchoolView(View):
    def get(self, request):

        

        return render(request, 'main/elements.html')

class BlogView(View):
    def get(self, request):

        get_blogs = Blog.objects.all()

        context = {
            'blogs':get_blogs
        }

        return render(request, 'main/blog-home.html', context) 
        
class BlogDetailView(View):
    def get(self, request, date, slug):

        get_blog = Blog.objects.get(date=date, slug=slug)

        comments = Comment.objects.filter(blog__date=date, blog__slug=slug)

        context = {
            'blog':get_blog,
            'form':CommentForm,
            'comments':comments
        }

        return render(request, 'main/blog-single.html', context)

    def post(self, request, date, slug):

        get_blog = Blog.objects.get(date=date, slug=slug)

        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)

            comment.blog = get_blog
            comment.user = request.user
            comment.save()

            return redirect('blog-detail',date=date, slug=slug)


class ContactView(View):
    def get(self, request):
        return render(request, 'main/contacts.html',{'authenticated_user_form':AuthenticatedUserContactForm,
                                                    'anonymous_user_form':AnonymousUserContactForm})

    def post(self, request):
        authenticated_user_form = AuthenticatedUserContactForm
        anonymous_user_form = AnonymousUserContactForm

        if request.user.is_authenticated:
            authenticated_user_form = AuthenticatedUserContactForm(request.POST or None)
            if authenticated_user_form.is_valid():

                contact = authenticated_user_form.save(commit=False)
                contact.user = request.user
                contact.save()

                messages.success(request, "Xabaringiz adminga yuborildi.")
                return redirect('contact')
        else:
            anonymous_user_form = AnonymousUserContactForm(request.POST or None)
            if anonymous_user_form.is_valid():

                anonymous_user_form.save()

                messages.success(request, "Xabaringiz adminga yuborildi.")
                return redirect('contact')
