from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.profile, name='profile'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^cat/(?P<pk>[0-9]+)/$', views.post_list_category, name='post_list_category'),
    url(r'^edit_profile/$', views.profile_edit, name='edit_profile'),
    url(r'^delpost/(?P<pk>[0-9]+)/$', views.DeletePost, name='DeletePost'),
    url(r'^add_post/$',views.add_post, name='AddPost')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

