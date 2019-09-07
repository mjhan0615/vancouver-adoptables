from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')

    def __str__(self):
        return self.name
