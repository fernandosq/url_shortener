from typing import List
from django.core.exceptions import ObjectDoesNotExist
from .models import URL


class CodeNotFound(Exception):
    pass


def save_new_code(old_url: str, code: str):
    """ Link and add to db a code to url """
    url = URL(
        full_url=old_url,
        url_code=code,
    )
    url.save()


def get_all_active_codes() -> [str]:
    """
    Get a list with all url codes
    """
    all_codes = URL.objects.values_list("url_code", flat=True)
    return all_codes


def get_code_url(code: str) -> URL:
    """
    Get a code of one url
    """
    try:
        url_object = URL.objects.get(url_code=code)
        return url_object

    except ObjectDoesNotExist as error_message:
        raise CodeNotFound(f"code {code} not found: {error_message}")


def increment_click_code(url_object: URL):
    """
    Method to increment clicks about one url, to make a ranking
    """
    url_object.clicks = url_object.clicks + 1
    url_object.save()


def top_ranking_clicks(number_top: int) -> List[URL]:
    """
    Method to get list of url with most clicks
    """
    clicks = URL.objects.all().order_by("clicks").reverse()[0:number_top + 1]
    return clicks






