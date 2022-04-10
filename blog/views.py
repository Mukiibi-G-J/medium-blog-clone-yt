from .form import EmailPostForm, CommentForm
from django.shortcuts import render, get_object_or_404
from .models import Post,Comments
from django.core.mail import send_mail


def list_view(request):
    posts = Post.published.all()
    context ={
    'posts':posts
    }
    return render(request,'blog/index.html', context)

def detail_view(request, month, year, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day) 
    
    # List of active comments for this post
        # Instead of building a
        # QuerySet for the Comment model directly, you leverage the post object to retrieve the
        # related Comment objects.

    comments = post.comments.filter(active=True)
   
    new_comments = None
    if request.method == "POST":
        commentform = CommentForm(data=request.POST)
        if commentform.is_valid():
            # this will creates an  object Comment  but will not save it to the databae
            new_comment = commentform.save(commit=False)
            
            # Assign the current post to the comment
            new_comment.post = post
            
            # Save the comment to the database
            new_comment.save()
    else:
        commentform = CommentForm()



    context={
      'post':post,
      'commentform':commentform,
      'new_comments':new_comments,
      'comments':comments
    }
     


    return render(request, 'blog/single-blog.html', context)
    



def share_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    if request.method=='POST':
        form =EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # post_url =
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you to read {post.title}"
            message = f"Read{post.title} at {post_url} \n {cd['name']}\'s comments:{cd['comment']}" 
            
            
            send_mail(subject, message, 'mukiibijosephgilbert865@gmail.com', [cd['to']])
    
    # if request.method == 'POST':
    else:
        form = EmailPostForm()
    return render(request, 'blog/form/form.html', {'form':form})

