from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from publication_app.forms.post_form import PostForm
from publication_app.models import Post


class PostsView(View):
    def get(self, request):
        posts = Post.objects.filter(is_public=True).order_by('-id').all()
        form = PostForm()

        context = {'post_form': form, 'posts': posts}
        return render(request, 'posts.html', context)

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(title=form.cleaned_data['title'], text=form.cleaned_data['text'])

        return redirect('/posts')
