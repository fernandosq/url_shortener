from django.db import models


class URL(models.Model):
    """
    Url base relational model
    This object stores the original provided url,
    the shortened code that relates to that url,
    a counter of how many times the shortened url was requested
    and a timestamp with the created date.
    """
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
