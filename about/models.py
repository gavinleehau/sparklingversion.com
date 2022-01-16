from django.db import models

# Create your models here.

class about(models.Model):
    fullName = models.CharField("Họ và Tên: ", default="", max_length=50)
    avatar = models.ImageField(null=True)
    description = models.TextField("Mô tả", default="", max_length=1000)
    faceBook = models.CharField("Facebook", default="", max_length=1000)
    twitter = models.CharField("Twiiter", default="", max_length=1000)
    instagram = models.CharField("Instagram", default="", max_length=1000)


    def __str__(self):
        return self.fullName

    class Meta:
        db_table = "about"

class contact(models.Model):
    location = models.CharField("Vị trí ", default="", max_length=100)
    phone = models.CharField("Số điện thoại ", default="", max_length=15)
    email_footer = models.CharField("Email ", default="", max_length=100)

    def __str__(self):
        return self.email_footer


