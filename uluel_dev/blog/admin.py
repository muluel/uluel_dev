from django.contrib import admin
from .models import Article, Comment
from django.db import models


  
class ArticleAdmin(admin.ModelAdmin):
   list_display = ["title"]
   # formfield_overrides = {
   # models.TextField: {'widget': TinyMCE()}
   # }

admin.site.register(Article, ArticleAdmin)

admin.site.register(Comment)