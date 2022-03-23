from django.shortcuts import render, redirect
from .models import TopBlog, Text, AddLesson, Blog, Author, Comment
from .forms import HomeForm, ElementForm, CommentForm, ContactForm
from django.http import HttpResponseRedirect, Http404
import random
from django.core.paginator import Paginator

def home(request):
    number = random.randint(1234567890, 1234567890123456789)
    saved = False
    if request.method == "POST":
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"?saved={number}")
    else:
        form = HomeForm
        if f'saved{number}' in request.GET:
            saved = True
    blog = Blog.objects.all()[4:]
    lessons = AddLesson.objects.all()
    return render(request,'index.html',{'form':form,'saved':saved,'blog':blog,'lessons':lessons})

def search(request):
    if request.method == "POST":
        searched = request.POST['search']
        values = AddLesson.objects.filter(subject__contains=searched)
        blog_values = Blog.objects.filter(title__contains=searched)
        return render(request, 'search.html',{'searched':searched, 'values':values,'blog_values':blog_values})
    else:
        return render(request, 'search.html',{})

def about(request):
    text = Text.objects.all()
    return render(request, 'about.html',{'text':text})
def courses(request):
    number = random.randint(1234567890, 1234567890123456789)
    saved = False
    if request.method == "POST":
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'?saved={number}')
    else:
        form = HomeForm
        if f'saved{number}' in request.GET:
            saved = True
    courses = AddLesson.objects.all()
    return render(request, 'courses.html',{'courses':courses,'saved':saved, 'form':form})

def elements(request):
    number = random.randint(1234567890, 1234567890123456789)
    saved = False
    if request.method == "POST":
        form = ElementForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'?saved={number}')

    else:
        form = ElementForm
        if 'saved' in request.GET:
            saved = True
    return render(request, 'elements.html',{'form':form, 'saved':saved})

def coursedetails(request):
    lessons = AddLesson.objects.all()
    return render(request, 'course-details.html',{'lessons':lessons})

def blog(request):
    authors = Author.objects.all()
    blogs = Blog.objects.all()

    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    users = paginator.get_page(page)
    nums = "a" * users.paginator.num_pages
    return render(request, 'blog-home.html',{'blogs':blogs,'authors':authors, 'getpages':users, 'nums':nums})

def author(request, author_id):
    author = Author.objects.get(pk=author_id)
    return render(request, 'author.html',{'author':author})

def lessons(request, lesson_id):
    lessons = AddLesson.objects.get(pk=lesson_id)
    lessons.views += 1
    lessons.save()
    return render(request, 'course-details.html',{'lessons':lessons})

def blogdetails(request,pk):
    saved = False
    blog = Blog.objects.get(pk=pk)
    comments = Comment.objects.filter(choose = blog)
     
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(name= form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            comment=form.cleaned_data['comment'],
            choose=blog)
            comment.save()
            return redirect(f'/blog/details/{pk}')
    else:
        form = CommentForm()
    authors = Author.objects.all()
    context = {
            'blog':blog,
            'form':form,
            'comments':comments,
            'form':form, 
            'authors':authors,
        }
    return render(request, 'blog-single.html',context)

def contacts(request):
    number = random.randint(1234567890, 1234567890123456789)
    saved = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'?saved={number}')

    else:
        form = ContactForm
        if f'saved{number}' in request.GET:
            saved = True
    return render(request, 'contacts.html',{'form':form, 'saved':saved})
