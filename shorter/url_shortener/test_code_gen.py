import itertools
import string
from.models import URL
from .code_gen import generate_short_url
from django.test import TestCase


class CodeGenTest(TestCase):
    def setUp(self) -> None:
        self.test_lengths = [2, 5, 6]

    def test_code_len(self):
        for size in self.test_lengths:
            code = generate_short_url(k=size)
            self.assertEqual(len(code), size)

    def test_is_letter_num(self):
        CODE_ITEMS = list(itertools.chain(string.digits, string.ascii_letters))
        code = generate_short_url(k=5)
        for letter_number in code:
            self.assertIn(letter_number, CODE_ITEMS)

