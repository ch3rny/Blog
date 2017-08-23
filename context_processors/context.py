from blog.models import UserProfile, Category, Post


def get_avatar(request):
    try:
        avatar = UserProfile.objects.get(user=request.user)
    except:
        avatar = 0
    return {'avatar': avatar}


def get_categories(request):
    categorys = Category.objects.all().order_by('category')
    for category in categorys:
        category.numbirs = (len(Post.objects.filter(category=category)))
    return {'categorys': categorys}
