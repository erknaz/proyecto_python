from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Category(models.Model):
    name=models.CharField(max_length=140)
    slug=models.SlugField(blank=True,null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title=models.CharField(max_length=140)
    slug=models.SlugField(blank=True,null=True)
    content=models.TextField()
    cover=models.ImageField(upload_to='images',blank=True, null=True)
    created_datetime=models.DateTimeField(default=timezone.now)
    categories=models.ManyToManyField(Category,related_name="posts")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug():
            self.slug=slugify(self.title)
        super().save(*args,**kwargs)


class Comment(models.Model):
    author=models.CharField(max_length=140)
    created_datetime=models.DateTimeField(default=timezone.now)
    text=models.TextField()
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)

    def __str__(self):
        return self.author
