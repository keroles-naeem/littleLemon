# tests/test_views.py
from rest_framework.test import APIClient
from django.test import TestCase
from ..models import MenuItem
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a test user
        self.user = User.objects.create_user(username='kero', password='1449')
        # Obtain a token for the user
        self.token = Token.objects.create(user=self.user)
        # Set the token in the client
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        # Create a few test instances of the MenuItem model
        self.menu_item1 = MenuItem.objects.create(title= "Ice Cream", price=80.00,inventory=100)
        self.menu_item2 = MenuItem.objects.create(title="Pizza", price=120.00,inventory=100)

    def test_getall(self):
        
        # Retrieve all MenuItem objects
        response = self.client.get(reverse('menu-items'))  # Adjust the URL name as needed
        print("this is data  :"+str(response.data))

        # Expected serialized data
        expected_data = [
            {
                # "id": self.menu_item1.id,
                'title': "Ice Cream",
                "price": '80.00',  # Adjust based on your serializer's output
                "inventory":int(100)
            },
            {
                # "id": self.menu_item2.id,
                "title": "Pizza",
                "price": '120.00',  # Adjust based on your serializer's output
                "inventory":int(100)

            }
        ]

        # Check if the response data matches the expected data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
        
        