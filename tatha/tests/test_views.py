from django.test import TestCase, Client
from django.urls import reverse
import json
from tatha.models import Tatha


class TestViews(TestCase):
     def test_index_list(self):
         response = self.client.get(reverse('index'))
         self.assertEqual(response.status_code,200)
         self.assertTemplateNotUsed(response,'tatha/index.html')