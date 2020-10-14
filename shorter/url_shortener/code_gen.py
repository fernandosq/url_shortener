import string
import itertools
from random import choices

CODE_ITEMS = list(itertools.chain(string.digits, string.ascii_letters))


def generate_short_url(k):
    while True:
        short_url = "".join(choices(CODE_ITEMS, k=k))
        yield short_url


def dani_gen(k):
    yield from (
        "".join(choices(CODE_ITEMS, k=k)) for _ in itertools.repeat(0)
    )