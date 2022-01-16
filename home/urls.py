from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='home' ),
    # url(r"^blog_detail/(?P<blog_id>[0-9]+)$",views.blogDetail, name="blog_detail"),
]