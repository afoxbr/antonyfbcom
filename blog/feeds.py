from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse

from .models import Post


class PostRSSFeed(Feed):
    title = 'Ramblings and Ruminations - AntonyFB'
    link = '/recentposts/'
    description = 'Recent posts about tech from AntonyFB'

    def items(self):
        return Post.objects.order_by('-date_added')[:25]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.text, 30)

    def item_link(self, item):
        return reverse('blog:post', args=[item.pk])
