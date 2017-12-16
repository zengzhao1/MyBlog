import markdown
from django.shortcuts import render,get_object_or_404
from .models import Post,Category
from comments.forms import CommentForm
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
def index(request):

    #文章集合 根据创建文章的时间排序
    post_list = Post.objects.all()

    paginator = Paginator(post_list,2)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:#用户请求页面不是整数,显示第一页
        posts = paginator.page(1)
    except EmptyPage:     #用户请求页面超过本身页面,显示最后一页
        posts = paginator.page(paginator.num_pages)
    return  render(request,'blog/index.html',context = {'posts' : posts})


#显示文章详细页面
def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)

    #每被阅读一次，阅读量+1
    post.increase_views()

    # 引入markdown
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc'
                                  ])
    form = CommentForm()
    #获取这篇文章下的全部评论
    comment_list = post.comment_set.all()

    #将文章,表单,评论列表作为变量床给detail.html模板
    context = {
        'post' : post,
        'form':form,
        'comment_list': comment_list
    }
    return render(request,'blog/detail.html',context=context)

#归档
def archives(request,year,month):
    #filter进行过滤
    post_list = Post.objects.filter(created_time__year = year,
                                    created_time__month = month
                                    )
    return render(request,'blog/index.html',context = {'post_list': post_list})

#分类
def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    #按照点击的分类名 进入其文章页面
    post_list = Post.objects.filter(category=cate)
    return render(request,'blog/index.html',context={'post_list':post_list})


