from django.shortcuts import render, redirect, get_object_or_404

from blog import forms
from blog.forms import BlogForm
from blog.models import Blog
from django.core.paginator import Paginator


def home_view(request):
    blogs = Blog.objects.all()  # objects all of Blog
    paginator = Paginator(blogs, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = BlogForm()
    context = {
        'page_obj': page_obj,
        'form': form,
        'blog_count': blogs.count(),
    }
    return render(request, 'blog/home.html', context)


def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-view')
        else:
            print(form.errors)
            return redirect('home-view')
    else:
        return redirect('home-view')


def detail(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    next_article = Blog.objects.filter(pk__gt=pk).order_by('pk').first()
    previous_article = Blog.objects.filter(pk__lt=pk).order_by('-pk').first()

    form = BlogForm()
    context = {
        'blog': blog,
        'next_article': next_article,
        'previous_article': previous_article,
        'form': form
    }
    return render(request, 'blog/detail.html', context)


def update(request):
    if request.method == 'POST':
        pk = request.POST['id']
        blog = get_object_or_404(Blog, id=pk)
        blog.title = request.POST.get('title')
        blog.description = request.POST.get('description')

        # Check if a new image is uploaded
        if 'image' in request.FILES:
            blog.image = request.FILES['image']

        blog.save()
        return redirect('detail', pk=pk)
    else:
        return render(request, 'blog/edit.html', {'form': BlogForm()})


def blog_delete(request):
    if request.method == 'POST':
        pk = request.POST.get('id')
        blog = get_object_or_404(Blog, id=pk)
        blog.delete()
        return redirect('home-view')


def blog_search(request):
    if request.method == "POST":
        q = request.POST.get('search')

        if not q:
            return redirect('home-view')

        page_obj = Blog.objects.filter(title__icontains=q)

        context = {
            'page_obj': page_obj,
            'form': BlogForm(),
        }
        return render(request, 'blog/home.html', context)

    return redirect('home-view')
