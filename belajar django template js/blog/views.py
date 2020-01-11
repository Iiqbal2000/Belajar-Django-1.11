from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):
    posts = Post.objects.all()
    kategoris = Post.objects.values('category').distinct()
    context = {
        'judul':'Home Blog',
        'kontenHal':'Ini adalah Home Blog',
        'kategoriLink':kategoris,
        'post':posts,

    }

    return render(request, 'blog/index.html', context)

def slugPost(request, slugInput):
    posts = Post.objects.get(slug=slugInput)
    context = {
        'judul':'Home Blog',
        'kontenHal':'Ini adalah Home Blog',
        'post':posts,
    }

    return render(request, 'blog/detail.html', context)

def kategoriPost(request, kategoriInput):
    posts = Post.objects.filter(category=kategoriInput)
    kategoris = Post.objects.values('category').distinct()
    context = {
        'judul':'Home Blog',
        'kontenHal':'tampilkan berdasarkan kategori',
        'kategoriLink':kategoris,
        'post':posts,
    }

    return render(request, 'blog/category.html', context)