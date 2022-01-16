from django.shortcuts import render
from about.models import about, contact
from blog.models import blog, author, decripsion
from photography.models import photo

# Create your views here.

def index(request):
    info = about.objects.get(pk=1)
    blogs = blog.objects.all().order_by('-id')[0:6]
    vote_count = blog.objects.all().count()
    photography_count = photo.objects.all().count()
    authors = author.objects.get(pk=1)
    home_decripsion = decripsion.objects.get(pk=1)
    contact_me = contact.objects.get(pk=1)

    return render (
        request=request,
        template_name = "index.html",
        context = {
            'info': info,
            'blogs': blogs,
            'vote_count': vote_count,
            'authors': authors,
            'photography_count': photography_count,
            'home_decripsion': home_decripsion,
            'contact_me': contact_me,
        }
    )

    
