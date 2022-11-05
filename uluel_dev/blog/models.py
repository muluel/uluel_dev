from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from uluel_dev.util import unique_slug_generator



class Article(models.Model):
  title = models.CharField(max_length=200)
  header_image = models.ImageField(upload_to='blogs', null=True, blank=True)
  content = tinymce_models.HTMLField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  slug = models.SlugField(max_length=255, verbose_name=('Url Slug'),blank=True, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
        return reverse("detail", args=[str(self.slug)])

  # def save(self, *args, **kwargs):
  #   self.slug = slugify(self.title)
  #   super(Article, self).save(*args, **kwargs)

@receiver(pre_save, sender=Article)
def pre_save_receiver(sender, instance, *args, **kwargs):
   if not instance.slug:
       instance.slug = unique_slug_generator(instance)


class Comment(models.Model):
  article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '%s - %s' % (self.post.title, self.name)


