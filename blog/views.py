
from django.shortcuts import render, get_object_or_404
from .models import Post


def list_view(request):
    posts = Post.published.all()
    return render(request,'blog/index.html',{'posts':posts})

def detail_view(request, month, year, date , post):
  
    post = get_object_or_404(Post, 
                             slug=post,
                             status='published' ,
                             publish__year=year, 
                             publish__date=date,
                             publish__month=month,
        
    )

