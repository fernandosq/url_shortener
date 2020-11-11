from django.db import models


class URL(models.Model):
    full_url = models.URLField()
    url_code = models.CharField(unique=True, max_length=32)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_url}, {self.url_code}, {self.clicks}, {self.created_at}"

    def clicked(self):
        self.clicks += 1
        self.save()

    def to_dict(self):
        return {
            "full_url": self.full_url,
            "url_code": self.url_code,
            "clicks": self.clicks,
            "created_at": self.created_at
        }
