from django.db import models


class URL(models.Model):
    full_url = models.URLField()
    url_code = models.CharField(unique=True, max_length=32)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def clicked(self):
        self.clicks += 1
        self.save()


