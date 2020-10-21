from django.http import HttpRequest, HttpResponse
from django.test import TestCase, Client
from .views import new
# Create your tests here.

class ViewNewTest(TestCase):

    def test_input_message(self):
        c = Client()
        response = c.post("/new/", {"url": "https://www.as.com"})
        self.assertEqual(response.status_code, 200)


