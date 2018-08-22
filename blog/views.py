
from django.shortcuts import render, get_object_or_404
from .models import Post
from taggit.models import Tag

def home(request):
 return render(request, 'home.html')

def index(request, tag_slug=None ):
 allpost = Post.objects.all()
 tag = None
 if 'category' in request.GET:

     allpost = allpost.filter(category=int(request.GET.get('category')))

 if tag_slug:

       tag = get_object_or_404(Tag, slug=tag_slug)
       allpost = allpost.filter(tags__in=[tag])

 return render(request,'index.html',{'posts': allpost.order_by('-created_on'), 'tag':tag })

def view_post(request, pk):
 post = Post.objects.get(pk=pk)

 return render(request, 'post.html', {'post': post})
