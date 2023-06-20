'''Define urls for blog app'''

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .feeds import PostRSSFeed


app_name = "blog"
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:post_id>/', views.post, name='post'),
    path('feed/rss', PostRSSFeed(), name="rss_feed"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
