from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author":"sarah",
        "title":"spiderman",
        "content":"post1-content",
        "date_posted":"1996"
    },
    {
        "author":"ali",
        "title":"batman",
        "content":"post2-content",
        "date_posted":"2006"
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request,"blog/home.html", context)

def about(request):
    return render(request,"blog/about.html")
