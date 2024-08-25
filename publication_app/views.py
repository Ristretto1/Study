from django.shortcuts import render

from .models import Post


# Create your views here.
def main_page(request):
    posts = Post.objects.filter(is_public=True).order_by('-id').all()

    context = {'title': 'I am title', 'posts': posts}
    return render(request, 'main_page.html', context)


def login(request):
    return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')
