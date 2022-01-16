from django.shortcuts import render
from .models import blog, decripsion, paragraph_blog, comment, CommentForm
from about.models import about, contact
from django.core.paginator import Paginator
from photography.models import photo
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def post(request):
    blogs = blog.objects.all()
    info = about.objects.get(pk=1)
    paragraph_body = paragraph_blog.objects.get(pk=1)
    vote_count = blog.objects.all().count()
    photography_count = photo.objects.all().count()

    new_paginator = Paginator(blogs, per_page = 5) #sô bài mỗi page
    page_number = request.GET.get('page') 
    page = new_paginator.get_page(page_number)

    contact_me = contact.objects.get(pk=1)

    return render (
        request=request,
        template_name = "blog.html",
        context = {
            'blogs': blogs,
            'info': info,
            'page':page,
            'new_paginator':new_paginator,
            'page_number': page_number,
            'paragraph_body': paragraph_body,
            'vote_count': vote_count,
            'photography_count': photography_count,
			'contact_me': contact_me,
        }
    )

def blogDetail(request, blog_id):
    blog_detail = blog.objects.get(id = blog_id)
    info = about.objects.get(pk=1)
    Latest_blogs = blog.objects.all().order_by('-id')[0:3]
    paragraph_body = paragraph_blog.objects.get(pk=1)
    comments = comment.objects.all()
    comment_count = comment.objects.all().count()
    
    return render(
        request = request,
        template_name="single.html",
        context={
            'blog_detail':blog_detail,
            'info': info,
            'Latest_blogs': Latest_blogs,
            'paragraph_body': paragraph_body,
            'comments': comments,
            'comment_count': comment_count
        }  
    )



def addcomment(request,id):
    url = request.META.get('HTTP_REFERER')  # get last url

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = comment()
            data.name = form.cleaned_data['name']
            data.body = form.cleaned_data['comment']
            data.blog_id=id
            data.save()  # save data to table
            messages.success(request, "Bài đánh giá của bạn đã được duyệt,Cảm ơn vì đã gửi đánh giá.")
            return HttpResponseRedirect(url)
    
    return HttpResponseRedirect(url)

# def addcomment(request,id):
#    	url = request.META.get('HTTP_REFERER')  # get last url

#    	if request.method == 'POST':  # check post
#       	form = CommentForm(request.POST)
#       	if form.is_valid(): 
#             data = comment()
#             data.body = form.cleaned_data['comment']
#             data.save()  # save data to table
#             messages.success(request, "Bài đánh giá của bạn đã được duyệt,Cảm ơn vì đã gửi đánh giá.")
#             return HttpResponseRedirect(url)

#    	return HttpResponseRedirect(url)


