from django.shortcuts import render
from .models import about

# Create your views here.

def information(request):
	info = about.objects.get(pk=1)

	return render(
		request = request,
		template_name='about.html',
		context={
			'info': info,
		}
	)
