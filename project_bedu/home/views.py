from django.shortcuts import render
from django.views import View
from .models import *

class HomeView(View):

    def get(self,request,*args,**kwargs):
        posts=Post.objects.all()
        return render(request,'home.html',locals())

class PostView(View):

    @property
    def pk(self,*args,**kwargs):
        return self.kwargs['pk']

    def get(self,request,*args,**kwargs):
        post=Post.objects.get(pk=self.pk)
        return render(request,'post.html',locals())

    def post(self,request,*args,**kwargs):
        post=Post.objects.get(pk=self.pk)
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
        return render(request,'post.html',locals())
