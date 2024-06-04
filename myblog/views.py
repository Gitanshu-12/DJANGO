from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore
from myblog.models import Post, Category
from django.contrib.auth import logout # type: ignore
from django.shortcuts import redirect # type: ignore
from django.views.decorators.http import require_POST # type: ignore







# Create your views here.


def home(request):
    # load all the post from db(10)
    posts = Post.objects.all()[:11]
    # print(posts)

    cats = Category.objects.all()

    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()

    # print(post)
    return render(request, 'posts.html', {'post': post, 'cats': cats})


def about(request):
    recent_posts = Post.objects.all()[:5]  # Get the 5 most recent posts
    return render(request, 'about.html', {'recent_posts': recent_posts})


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'posts': posts})

def contact(request):
    return render(request, 'contact.html')