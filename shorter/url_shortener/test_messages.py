from django.test import TestCase
from .messages import NewResponseMessage


class NewResponseMessageTest(TestCase):
    def setUp(self):
        self.code = "aaa"

    def test_serialize(self):
        response = NewResponseMessage(self.code)
        json = response.serialize()
        self.assertEqual(dict, type(json))
        self.assertEqual(json, {"code": self.code})