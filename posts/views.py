from django.shortcuts import render, get_object_or_404
from .models import Post



# Create your views here.
def post_list(req):
    posts = Post.objects.all()
    return render(req, 'posts/post_list.html', {'posts': posts})


def post_details(req, id):
    posts = Post.objects.all()
    post = get_object_or_404(Post, id=id)
    return render(req, 'posts/post_details.html', {'post': post, 'posts': posts})
