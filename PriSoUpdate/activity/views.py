from django.shortcuts import render, redirect
from .form import Postcreateform,commentcreateform
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from .models import Post
def post_create(request):
    post=None
    if request.method == 'POST':
        form = Postcreateform(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.profile
            post.save()
            return redirect('dashboard')

    else:
        form = Postcreateform()

    return render(
        request,
        'activity/post/post.html',
        {'form': form,'post':post}
    )


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    comment = None
    form = commentcreateform(data=request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user.profile
        comment.save()
        return redirect('dashboard')

    