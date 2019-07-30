from django.db import models


class movie(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    year = models.IntegerField(blank=False)
    genre = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        options = self.title and {'title': self.title} or {}
        super(movie, self).save(*args, **kwargs)