import itertools
import string
from .code_gen import generate_short_url, OverLimitError, generate_unique_code
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


class CodeGenUnique(TestCase):
    def test_unable_to_generate_code(self):
        self.assertRaises(OverLimitError, generate_unique_code, k=4, all_codes=[], limit=0)



