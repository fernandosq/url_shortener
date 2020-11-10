from django.http import HttpRequest, HttpResponse
from django.test import TestCase, Client
from http import HTTPStatus

from .db import save_new_code
from .views import new
# Create your tests here.


class ViewNewTest(TestCase):

    def test_valid_url(self):
        response = self.client.post("/new/", {"url": "https://www.as.com"}, content_type="application/json")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_invalid_url(self):
        response = self.client.post("/new/", {"url": "hppts://www.as.com"}, content_type="application/json")
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_request_method(self):

        response = self.client.get("/new/", {"url": "https://www.as.com"})
        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)


class ViewCodeToUrlTest(TestCase):
    def setUp(self) -> None:
        self.url = "https://www.as.com"
        self.code = "aaaaaa"
        save_new_code(self.url, self.code)

    def test_redirect(self):
        response = self.client.get(f"/{self.code}")
        self.assertEqual(response.status_code, HTTPStatus.MOVED_PERMANENTLY)
        self.assertEqual(self.url, response.url)

    def test_request_method(self):
        response = self.client.post(f"/{self.code}")
        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

    def test_code_not_found(self):
        response = self.client.get("ababa")
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)


class RankingTest(TestCase):
    def test_request_method(self):
        response = self.client.post("/ranking/")
        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

    def test_request_ok(self):
        self.url = "https://www.as.com"
        self.code = "aaaaaa"
        save_new_code(self.url, self.code)
        response = self.client.get("/ranking/")
        json_response = response.json()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(json_response), 1)





