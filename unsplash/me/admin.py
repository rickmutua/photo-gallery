from django.contrib import admin
from .models import Editor, Post, Tags

# Register your models here.


admin.site.register(Editor)
admin.site.register(Post)
admin.site.register(Tags)