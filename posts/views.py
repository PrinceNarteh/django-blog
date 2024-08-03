from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Post



# Create your views here.
def post_list(req):
    posts = Post.objects.all()
    return render(req, 'posts/post_list.html', {'posts': posts})


def post_details(req, id):
    valid_id = False
    for item in posts:
        if item['id'] == id:
            post = item
            valid_id = True
    if valid_id:
        return render(req, 'posts/post_details.html', {'post': post, 'posts': posts})
    else:
        return HttpResponseNotFound('Post Not Found')
