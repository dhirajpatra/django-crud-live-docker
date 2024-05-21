# tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User
from .serializers import UserSerializer

class UserAPITestCase(APITestCase):

    def test_get_all_users(self):
        """
        Test that GET request to /users returns all users.
        """
        response = self.client.get(reverse('get_users'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_user(self):
        """
        Test that GET request to /users/{pk} returns a specific user.
        """
        user = User.objects.create(username="test_user", email="test@example.com")
        url = reverse('get_user', kwargs={'pk': user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        """
        Test that POST request to /users creates a new user.
        """
        data = {"username": "new_user", "email": "new@example.com"}
        response = self.client.post(reverse('add_user'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_update_user(self):
        """
        Test that PUT request to /users/{pk} updates a user.
        """
        user = User.objects.create(username="test_user", email="test@example.com")
        url = reverse('update_user', kwargs={'pk': user.pk})
        data = {"username": "updated_user", "email": "updated@example.com"}
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user.refresh_from_db()
        self.assertEqual(user.username, "updated_user")
        self.assertEqual(user.email, "updated@example.com")

    def test_delete_user(self):
        """
        Test that DELETE request to /users/{pk} deletes a user.
        """
        user = User.objects.create(username="test_user", email="test@example.com")
        url = reverse('delete_user', kwargs={'pk': user.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(pk=user.pk).exists())
