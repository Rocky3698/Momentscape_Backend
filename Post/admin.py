from django.contrib import admin
from .models import Post, React, Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(React)
admin.site.register(Comment)