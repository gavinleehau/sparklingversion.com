from django.urls import path, re_path

from . import views


urlpatterns = [
    path('', views.post, name='blog' ),
    re_path(r"^blog_detail/(?P<blog_id>[0-9]+)$",views.blogDetail, name="blog_detail"),
    path('addcomment/<int:id>', views.addcomment, name='addcomment'),
]