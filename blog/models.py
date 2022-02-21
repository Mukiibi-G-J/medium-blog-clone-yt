
# from django.db import models
# from django.contrib.auth.models import User
# from django.urls import reverse
# from django.utils import timezone


# class MyManger(models.Manager) :
#     def get_queryset(self):
#      return super().get_queryset() .filter(status='published')


# class Post(models.Model):
   
#     STATUS_CHOICES = (
#         ('draft', 'Draft',),
#         ('published', 'Published',)
#     )
#     title = models.CharField(max_length=255)
#     publish = models.DateTimeField(default=timezone.now)
#     slug = models.SlugField(max_length=255, unique_for_date='published')
#     body = models.TextField(max_length=255)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts' )
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='Draft')
#     objects = models.Manager() #default manager
#     published = MyManger() #
   
#    #Canonical urls
#     def get_absolute_url(self):
#         return reverse('blog:detail_view', args=[self.publish.year, self.publish.month, self.publish.day])
    
#     class Meta:
#         ordering = ('-publish',)
    
#     def __str__(self):
#         return self.title



from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail_view',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])
