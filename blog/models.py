from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
from django.forms import ModelForm

# Create your models here.

class author(models.Model):
    fullname = models.CharField("Tên tác giảaaa", default="", max_length=30)
    avatar = models.ImageField(null=True)

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = "author"


class blog(models.Model):
    author_name =  models.ForeignKey(author, on_delete=models.CASCADE)
    title = models.CharField("Tiêu đề", default="", max_length=100)
    hashtag = models.CharField("hashtag", default="", max_length=100)
    date = models.DateField("Thời gian đăng")
    content = RichTextUploadingField("Nội dung")
    image = models.ImageField(null=True)
    label = "Bài viết"

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        db_table = "blog"


class comment(models.Model):
    post = models.ForeignKey(blog, on_delete=models.CASCADE)
    name = models.CharField("Tên", default="", max_length=100)
    body = models.TextField("Bình luận")
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class CommentForm(ModelForm):
    class Meta:
        model = comment
        fields = ['name', 'body']



class decripsion(models.Model):
    note = models.CharField("Note", default="", max_length=100)
    decripsion = models.TextField("Mô tả", default="")

    def __str__(self):
        return self.note

    class Meta:
        ordering = ['-id']
        db_table = "decripsion"

class paragraph_blog(models.Model):
    note_paragraph = models.CharField("Note", default="paragraph", max_length=100)
    paragraph = models.TextField("paragraph", default="")

    def __str__(self):
        return self.note_paragraph

