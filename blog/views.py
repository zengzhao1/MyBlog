import markdown
from django.shortcuts import render,get_object_or_404
from .models import Post,Category
def index(request):

    #文章集合 根据创建文章的时间排序
    post_list = Post.objects.all().order_by('created_time')
    return  render(request,'blog/index.html',context = {'post_list':post_list})

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)

    # 引入markdown
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc'
                                  ])
    return render(request,'blog/detail.html',context={'post': post})

#归档
def archives(request,year,month):
    #filter进行过滤
    post_list = Post.objects.filter(created_time__year = year,
                                    created_time__month = month,
                                    ).order_by('created_time')
    return render(request,'blog/index.html',context = {'post_list': post_list})

#分类
def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    #按照点击的分类名 进入其文章页面
    post_list = Post.objects.filter(category=cate).order_by('created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

