''' Models for blog '''
from django.db import models
from django.contrib.auth.models import User


class Postcategory(models.Model):
    ''' Category model for Blog Post '''
    class Meta:
        verbose_name_plural = 'Postcategories'

    name = models.SlugField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    ''' Post model for Blog app '''
    postcategory = models.ForeignKey('Postcategory', null=True, blank=True,
                                     on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=150, default='')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ''' order posts by reverse date '''
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    ''' Comment model for Blop app '''
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ''' order comments by reverse date '''
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
