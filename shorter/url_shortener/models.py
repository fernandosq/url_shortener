

from django.db import models

# Create your models here.

class URL(models.Model):
    full_url = models.URLField(unique=True)
    short_url = models.URLField(unique=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def clicked(self):
        self.clicks += 1
        self.save()


