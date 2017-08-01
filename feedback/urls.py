from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views


urlpatterns = [
                  url(r'^feedback/$', views.ReviewCreate, name='review'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
