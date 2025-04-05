from django.db import models
from django.contrib.auth.models import User  # To associate posts with users

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Post Title")
    description = models.TextField(verbose_name="Post Description")
    image = models.ImageField(upload_to='static/upload_images', null=True, blank=True, verbose_name="Post Image")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last Update")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts',default=None)

    class Meta:
        ordering = ['-created_at']  # Newest posts first

    def __str__(self):
        return self.title