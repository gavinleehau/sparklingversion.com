from django.contrib import admin
from blog.models import blog, author, paragraph_blog, comment

# Register your models here.

admin.site.register(author)
admin.site.register(blog)
admin.site.register(paragraph_blog)
admin.site.register(comment)

