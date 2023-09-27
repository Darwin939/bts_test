from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book

class BookAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')

    def test_create_book(self):
        data = {
            "title": "Test Book",
            "publisher": "Test Publisher",
            "author": "Test Author",
            "pages": 200,
            "created_at": "2023-01-01T00:00:00+03:00",
            "updated_at": "2023-01-01T00:00:00+03:00",
            "tags": ["Test", "API"]
        }
        response = self.client.post('/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Test Book')
