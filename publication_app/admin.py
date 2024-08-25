from django.contrib import admin

from publication_app.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'title')
    ordering = ('id',)
    readonly_fields = ('created_at',)