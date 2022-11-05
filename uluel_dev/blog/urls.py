from django.urls import path 
from .views  import Index, detail


urlpatterns = [
  path('', Index.as_view(), name='index'),
  path('<slug>', detail,name='detail')
  # path('<slug>', Post.as_view(), name='post'),
]
