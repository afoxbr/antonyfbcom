'''Define urls for blog app'''

from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:post_id>/', views.post, name='post'),
]
