from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Post
from .forms import PostModelForm

def post_list_old(request):
    name_var='Django장고'
    return HttpResponse('''<h2>Hello {name}</h2>
    '''.format(name=name_var))

def post_list(request):
    posts_list = Post.objects.filter(published_date__lte=timezone.now())\
    .order_by('created_date')
    return render(request,'blog/post_list.html',{'posts':posts_list})

def post_detail(request,pk):
    post_obj = get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post_obj})

def post_new(request):
    if request.method == "POST":
        myform = PostModelForm(request.POST)
        if myform.is_valid():
            print(myform.cleaned_data)
            post = myform.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        #GET 요청 일때 입력 폼을 출력
        myform = PostModelForm()
    return render(request,'blog/post_edit.html',{'form':myform})