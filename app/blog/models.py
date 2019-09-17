from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

# post status
STATUS = (
    (0, "Draft"),
    (1, "Publish"),
    (2, "Un-publish")
)
COMMENT_STATUS = (
    (0, "Waiting for approval"),
    (1, "Publish"),
    (2, "Block")
)

""" post category model class"""


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=255, blank=True, default='')
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_categories', args=[str(self.slug)])

    def __str__(self):
        return self.title


"""Post Tag model class"""


class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=255, blank=True, default='')
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_tags', args=[str(self.slug)])

    def __str__(self):
        return self.name


"""Post model class"""


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True, default='')
    image = models.ImageField(default='', blank=True, upload_to='images')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(350, 200)],
                                     format='JPEG',
                                     options={'quality': 60})
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    pub_date = models.DateTimeField('date published')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, related_name='posts')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.slug)])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_on']


"""Post comment"""


class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
    status = models.IntegerField(choices=COMMENT_STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
