import string
import itertools
from random import choices
from typing import List


class OverLimitError(Exception):
    pass


CODE_ITEMS: List[chr] = list(itertools.chain(string.digits, string.ascii_letters))


def generate_short_url(k: int) -> str:
    """Method to generate string formed by letters and numbers whose length is K"""
    short_url = "".join(choices(CODE_ITEMS, k=k))
    return short_url


def generate_unique_code(k: int, all_codes: List[str], limit: int) -> str:
    """
    Generate a unique code checking if it was not generated before
    """
    counter = 0
    while counter < limit:
        counter = counter + 1
        code = generate_short_url(k)
        if code not in all_codes:
            return code

    raise OverLimitError("All generates codes are in the db")
