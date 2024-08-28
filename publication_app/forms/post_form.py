from django.forms import ModelForm

from publication_app.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')
