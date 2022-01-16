from django.db import models

# Create your models here.

class photo(models.Model):
    note = models.CharField("Chú thích hình ảnh", default='note photo', max_length=50, null=False)
    images = models.ImageField(null=True)
    name_location = models.CharField("Tên địa điểm", default='', max_length=20, null=False)
    location = models.CharField("Vị trí", default='', max_length=10, null=False)

    def __str__(self):
        return self.note

    class Meta:
        ordering = ['-id']
        db_table = "photo"
