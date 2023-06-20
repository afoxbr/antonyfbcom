from django.db import models


class Tag(models.Model):

    # tags to help organise/search for blog posts
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Post(models.Model):

    # the posts themselves
    title = models.CharField(max_length=200, unique=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
