from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):

    """
    分类(category)
    """
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    标签(Tag)
    """
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Post(models.Model):
    """
    Post(文章)
    """
    #标题
    title = models.CharField(max_length = 80)

    #文章正文
    body = models.TextField()

    #文章创建时间    文章更新时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    #文章摘要  可空
    excerpt = models.CharField(max_length = 200,blank=True)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank = True)

    #作者
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})


