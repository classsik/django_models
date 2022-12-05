from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True)