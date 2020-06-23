from django.db import models

# Create your models here.


class Gallery(models.Model):
    description = models.CharField(default='作品的描述', max_length=100)
    image = models.ImageField(default='default.png', upload_to='images/')
    title = models.CharField(default='作品的标题', max_length=20)
    def __str__(self):
        return self.title
