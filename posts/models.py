from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


'''
    - html widget
    - validations
    - best for data base
'''
# Create your models here.
# create data base    by   model    هو عبارة عن حارس على قاعدة البيانات  والمسئول عن تحويل كود بايثون إلى كود قاعدة البيانات سيكوال
class Post(models.Model):           
    title=models.CharField(max_length=100,verbose_name=_('name_post'))
    content=models.TextField(_('content'),max_length=1000)
    draft=models.BooleanField(_('draft'),default=True)
    publish_date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author')
    #author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_set')
    image=models.ImageField(upload_to='photo/%y-%m-%d')
    tags = TaggableManager()
    slug=models.SlugField(null=True,blank=True)
    category=models.ForeignKey('Category',on_delete=models.CASCADE,related_name='post_category')



    def __str__(self):
        return self.title
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comment_post')
    content=models.TextField(max_length=500)
    author=models.CharField(max_length=100)
    publish_date=models.DateTimeField(auto_now=True)

    def __srt__(self):
        return str(self.post)



