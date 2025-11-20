from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    author = models.CharField(max_length=100, default="Winson")  # or blank=True
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ["-published", "-created_at"]  # newest first

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # auto-generate slug from title if empty
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
