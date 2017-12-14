from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm

def post_comment(request,post_pk):
    #获取被评论的文章
    post = get_object_or_404(Post,pk=post_pk)

    if request.method == 'POST':#用户提交数据
        form = CommentForm(request.POST)

        if form.is_valid():#合法
            comment = form.save(commit=False)

            #将评论和评论文章关联
            comment.post = post
            #保存进数据库
            comment.save()
            #重定向到详情页
            return redirect(post)

        else:

            comment_list = post.comment_set.all()
            context = {'post' : post,
                       'form' : form,
                       'comment_list' : comment_list,
            }
            return render(request,'blog/detail.html',context=context)
    #用户没有提交数据
    return redirect(post)
