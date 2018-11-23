from django.db import models

# Create your models here.

class TourismConfig(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
