from .models import URL


def save_new_code(old_url, code):
    url = URL(
        full_url=old_url,
        url_code=code,
    )
    url.save()