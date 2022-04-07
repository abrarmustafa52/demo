from django.test import TestCase
 

from .models import sports
from django.db.models import Count

# Create your tests here.
class SportsViewTest(TestCase):

    def test_isvalid_nplayers(self):
        response = self.client.get("/nplayers")
        self.assertEqual(response.status_code, 200)

    def test_isvalid_noplayers(self):
        response = self.client.get("/nplayers")
        self.assertEqual(response.status_code, 200)
