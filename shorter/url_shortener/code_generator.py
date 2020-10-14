import string
import itertools
from random import choices

def generate_short_url(k):
    characters = itertools.chain(string.digits, string.ascii_letters)
    short_url = "".join(choices(characters, k=k))
    return short_url