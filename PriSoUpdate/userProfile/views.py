from django.shortcuts import render,redirect
from .models import Profile, Follow
from activity.models import Post
from .form import ProfileUpdateForm,LoginForm,UserRegistrationForm,UserEditForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def profile_view(request,username):
    profile = get_object_or_404(
        Profile,
        user__username=username
    )
    posts = profile.posts.all()
    following_ids = set(
        request.user.profile.following.values_list(
            'following_id',
            flat=True
        )
    )
    return render(
        request,
        'account/profile.html',
        {'profile':profile,
         'posts':posts,
         'following_ids': following_ids,
        }             
    )
    
@login_required
def unfollow_user(request, username):

    target = get_object_or_404(
        Profile,
        user__username=username
    )

    Follow.objects.filter(
        follower=request.user.profile,
        following=target
    ).delete()

    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))

@login_required
def follow_user(request, username):

    target = get_object_or_404(
        Profile,
        user__username=username
    )

    me = request.user.profile

    if me != target:
        Follow.objects.get_or_create(
            follower=me,
            following=target
        )

    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))


@login_required
def edit(request):
    profile, created = Profile.objects.get_or_create(
        user=request.user
    )
    if request.method=="POST":
        user_form = UserEditForm(
            instance=request.user,
            data=request.POST
        )
        profile_form = ProfileUpdateForm(
            instance=profile,
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect(
                'profile',
                username=request.user.username
            )
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)
        return render(
            request,
            'account/edit.html',
            {'user_form': user_form,
            'profile_form': profile_form
            }
        )
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        else:
            form = LoginForm()
            return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    profile = request.user.profile
    posts = Post.objects.all()

    following = [
        f.following
        for f in profile.following.all()
    ]

    following_ids = set(
        profile.following.values_list(
            'following_id',
            flat=True
        )
    )

    for post in posts:
        post.is_following = post.author.id in following_ids

    return render(
        request,
        'account/dashboard.html',
        {
            'section': 'dashboard',
            'profile': profile,
            'posts': posts,
            'following': following,
            'following_ids' : following_ids,
        }
    )


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(
               request,
               'account/register_done.html',
               {'new_user': new_user}
           )
    else:
        user_form = UserRegistrationForm()
    return render(
        request,
        'account/register.html',
        {'user_form': user_form}
    )
# Create your views here.
