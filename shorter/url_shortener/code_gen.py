import string
import itertools
from random import choices


CODE_ITEMS = list(itertools.chain(string.digits, string.ascii_letters))


def generate_short_url(k):

    short_url = "".join(choices(CODE_ITEMS, k=k))
    return short_url


def generate_unique_code(k, all_codes):
    while True:
        code = generate_short_url(k)
        if code not in all_codes:
            return code
