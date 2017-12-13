from ..models import Post,Category
from django import template

register = template.Library()

@register.simple_tag
#获取数据库前5篇文章
#最新文章模板
def get_recent_post(num=5):
    return Post.objects.all().order_by('created_time')[:num]

#归档模板标签
@register.simple_tag
def archives():
    return Post.objects.dates('created_time','month',order='DESC')#DESC表示降序,越近排在越前

#分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.all()

