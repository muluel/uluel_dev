from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article
from django.http import HttpResponse

class Index(ListView):
  model = Article
  template_name = 'blog/blog.html'
  # context={
  #   'articles' : articles,
  # }
  # return render(request,'blog/blog.html', context)

# def post(request,id):
#   post = Article.objects.get(id=id)

#   context={
#     'items' : post,
#   }
#   return render(request,'blog/blog.html', context)

# class Post(DetailView):
#   model= Article
#   template_name = 'blog/post.html'

def detail(request, slug):
  q = Article.objects.filter(slug__iexact = slug)
  if q.exists():
    q = q.first()
  else:
    return HttpResponse('<h1>Post Not Found</h1>')
  context = {
 
    'object': q
  }
  return render(request, 'blog/post.html', context)