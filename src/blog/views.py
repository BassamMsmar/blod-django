from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import  NewComment, forms
# Create your views here.

def home(request):
    posts = Post.objects.all()
    context ={
        'title':'الصفحة الرئيسية',
        'posts': posts
        }
    return render(request, 'blog/index.html', context)

def about_us(request):
    return render(request, 'blog/about-us.html', {'title': 'من نحن '})



def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(active=True)
    
    if request.method == 'POST':
        comment_form = NewComment(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            # comment_form = NewComment()
            return redirect('detail', post_id)
    else:
        comment_form = NewComment()
        

    comment_form = NewComment()
    context ={
        'title': post,
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    }
    
    return render(request, 'blog/detail.html', context)



# def post(request):
    
#     context = {'posts': posts}
#     return render(request, 'blog/index.html', context)


