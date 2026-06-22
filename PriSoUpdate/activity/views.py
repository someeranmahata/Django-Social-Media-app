from django.shortcuts import render, redirect
from .form import Postcreateform

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