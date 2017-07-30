from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Category, UserProfile, Comment
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from .forms import AddComment, EditProfile, EditUserPic, AddPost


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    categorys = Category.objects.all().order_by('category')
    for category in categorys:
        category.numbirs = (len(Post.objects.filter(category=category)))
    current_user=request.user
    avatar = 0
    if request.user.is_authenticated():
        avatar = UserProfile.objects.get(user=current_user)
    return render(request, 'blog/post_list.html', {'posts': posts,
                                                   'categorys':categorys,
                                                   'current_user':current_user,
                                                   'avatar':avatar})


def post_list_category(request, pk):
    cat=get_object_or_404(Category,pk=pk)
    posts = Post.objects.filter(category=cat).order_by('-published_date')
    categorys = Category.objects.all().order_by('category')
    for category in categorys:
        category.numbirs = (len(Post.objects.filter(category=category)))
    current_user=request.user
    avatar = 0
    if request.user.is_authenticated():
        avatar = UserProfile.objects.get(user=current_user)
    return render(request, 'blog/post_list.html', {'posts': posts,
                                                   'categorys':categorys,
                                                   'current_user':current_user,
                                                   'avatar':avatar})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    categorys = Category.objects.all().order_by('category')
    author = get_object_or_404(UserProfile, user = post.author)
    current_user = request.user
    form = AddComment()
    if request.method == "POST":
        form = AddComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.author_avatar = UserProfile.objects.get(user=current_user)
            comment.created_date = timezone.now()
            comment.sourse = post.title
            comment.save()
        else:
            form = AddComment()
    comments = Comment.objects.filter(sourse=post.title)
    count = len(comments)
    for category in categorys:
        category.numbirs = (len(Post.objects.filter(category=category)))

    avatar = 0
    if request.user.is_authenticated():
        avatar = UserProfile.objects.get(user=current_user)

    likes_count = post.likes.count()
    post.watched+=1
    post.save()
    return render(request, 'blog/post_detail.html', {'post': post,
                                                     'categorys':categorys,
                                                     'current_user':current_user,
                                                     'avatar':avatar,
                                                     'form': form,
                                                     'comments':comments,
                                                     'count':count,
                                                     'author':author,
                                                     'likes_count':likes_count
                                                     })


def handler404(request):
    response = render_to_response('blog/404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            profile = UserProfile(user=request.user)
            profile.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


def profile(request, pk):
    account = get_object_or_404(User, pk=pk)
    pr_image = UserProfile.objects.get(user=account)
    avatar = UserProfile.objects.get(user=request.user)
    posts = Post.objects.filter(author=account).order_by('-published_date')
    return render(request, 'blog/profile_view.html',{'account':account,
                                                     'pr_image':pr_image,
                                                     'avatar':avatar,
                                                     'posts':posts})


def profile_edit(request):
    user = request.user
    userpic = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":
        usrform = EditProfile(request.POST, instance=user)
        picform = EditUserPic(request.FILES, instance=userpic)
        if usrform.is_valid() and picform.is_valid() :
            user = usrform.save()
            userpic =picform.save(commit=False)
            userpic.user = user
            if 'profile_image' in request.FILES:
                userpic.profile_image = request.FILES['profile_image']
            userpic.save()
            return redirect('profile', pk=request.user.pk)
        else:
            return render_to_response('blog/profile_edit.html', {
                'usrform': usrform,
                'picform':picform,
                },
                context_instance=RequestContext(request))
    else:
        usrform = EditProfile(instance=user)
        picform = EditUserPic(request.FILES)
        return render(request, "blog/profile_edit.html", {
            'usrform': usrform,
            'picform': picform,
            })


def DeletePost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


def add_post(request):
    post = Post()
    form = AddPost(request.POST)
    if request.method == "POST":
        form = AddPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.published_date = post.created_date
            if 'cover' in request.FILES:
                post.cover = request.FILES['cover']
            post.save()
            return redirect('post_list')
        else:
            return redirect('profile', pk=request.user.pk)
    return render(request, 'blog/add_post.html', {'form':form,})


def EditPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = AddPost(instance=post)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.published_date = post.created_date
            post.save()
            return redirect('post_list')
        else:
            return redirect('profile', pk=request.user.pk)
    return render(request, 'blog/add_post.html', {'form':form,})


def LikePost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = get_object_or_404(UserProfile, user=request.user)
    if post.likes.filter(user=request.user).exists():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return redirect('post_detail', pk=post.pk)
