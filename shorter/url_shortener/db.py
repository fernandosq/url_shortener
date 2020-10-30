from .models import URL


def save_new_code(old_url, code):
    url = URL(
        full_url=old_url,
        url_code=code,
    )
    url.save()
def get_all_active_codes() -> [str]:
    all_codes = URL.objects.values_list("url_code", flat=True)
    return all_codes

