from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    intro = models.CharField(max_length=200)
    content = models.TextField()
