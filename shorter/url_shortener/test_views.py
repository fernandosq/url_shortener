from django.http import HttpRequest, HttpResponse
from django.test import TestCase, Client
from http import HTTPStatus
from .views import new
# Create your tests here.


class ViewNewTest(TestCase):

    def test_valid_url(self):
        response = self.client.post("/new/", {"url": "https://www.as.com"}, content_type="application/json")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_invalid_url(self):
        response = self.client.post("/new/", {"url": "hppts://www.as.com"}, content_type="application/json")
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)


