from django.contrib import admin
from .models import Article, Comment

# We register our models here so they show up in the Django Admin panel.
# This gives us a beautiful interface to create, edit, and delete data without writing SQL.

# Registering 'Article' lets us manage our blog posts.
admin.site.register(Article)

# Registering 'Comment' lets us manage feedback left by readers.
admin.site.register(Comment)
