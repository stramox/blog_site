from lib2to3.fixes.fix_input import context

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404

from .forms import NewPostForm
from .models import Post

def post_list_view(request):
    posts_list = Post.objects.all()
    context = {"posts_list": posts_list}
    return render(request, "blog/posts_list.html", context)


def post_detail_view(request, pk):
    # try:
    #     post = Post.objects.get(pk=pk)
    # except ObjectDoesNotExist.DoesNotExist:
    #     post = None
    #     print("excepted")
    # return render(request, 'blog/post_detail.html', {"post": post})

        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {"post": post})

def post_create_view(request):
    # #  return render(request, 'blog/post_create.html')
    # # print(request.method)
    # # print(request.POST)
    # if request.method == "POST":
    # #     print('post')
    # #
    # # else:
    # #     print('get request')
    #
    #     post_title = request.POST.get('title')
    #     post_text = request.POST.get('text')
    #     user = User.objects.all()[0]
    #     Post.objects.create(title= post_title, description=post_text, author=user, status = 'pub')
    #
    #
    # else:
    #     print('get request')
    #
    # return render(request, 'blog/post_create.html')
    if request.method == 'POST':
        #pass

        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()


