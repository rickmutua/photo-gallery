from django.contrib import admin
from .models import Editor, Post, Tags

# Register your models here.


class PostAdmin(admin.ModelAdmin):

    filter_horizontal = ('tags',)


admin.site.register(Editor)
admin.site.register(Post, PostAdmin)
admin.site.register(Tags)