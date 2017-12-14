from django.db import models

class Comment(models.Model):
    #评论用户姓名
    name = models.CharField(max_length=100)
    #评论用户email
    email = models.EmailField(max_length=255)
    #评论时间
    created_time = models.DateTimeField(auto_now_add=True)
    #评论内容
    text = models.TextField()

    post = models.ForeignKey('blog.Post')

    #返回用户的评论
    def __str__(self):
        return self.text[:20]

