from django.shortcuts import render
from .models import photo
from blog.models import blog
from about.models import contact

# Create your views here.
def photography(request):
    photos = photo.objects.all()
    contact_me = contact.objects.get(pk=1)

    vote_count = blog.objects.all().count()
    photography_count = photo.objects.all().count()

    return render(
        request = request,
        template_name='photography.html',
        context={
            'photos': photos,
            'photography_count': photography_count,
            'vote_count': vote_count,
            'contact_me': contact_me,
        }
  	)



