from django.test import TestCase
from .messages import NewResponseMessage,RankingResponseMessage
from .models import URL


class NewResponseMessageTest(TestCase):
    def setUp(self):
        self.code = "aaa"

    def test_serialize(self):
        response = NewResponseMessage(self.code)
        json = response.serialize()
        self.assertEqual(dict, type(json))
        self.assertEqual(json, {"code": self.code})


class RankingResponseMessageTest(TestCase):
    def setUp(self):
        self.url_object = URL(
            full_url="https://as.com/",
            url_code="aaa",
            clicks=6,
            created_at="2020-11-05T10:29:38.974Z"
        )
        self.clicks = [
            self.url_object
        ]

    def test_serialize(self):
        response = RankingResponseMessage(self.clicks)
        json = response.serialize()
        print(json)
        dict_setup = {
            "ranking": [{
            "full_url": "https://as.com/",
            "url_code": "aaa",
            "clicks": 6,
            "created_at": "2020-11-05T10:29:38.974Z",}]
        }
        print(dict_setup)
        self.assertEqual(dict, type(json))

        self.assertEqual(json, dict_setup)