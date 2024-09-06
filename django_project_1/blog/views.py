from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from blog.models import Post
from blog.forms import PostCreateForm

def home(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if not form.is_valid():
            return render(
                request,
                'home.html',
                {
                    'form': form,
                    'posts': Post.objects.all(),
                }
            )
        form.save()


    return render(
        request, 
        'home.html',
        {
            'form': PostCreateForm(),
            'posts': Post.objects.all(),
        }
    )

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')

