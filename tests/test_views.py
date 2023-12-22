from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        item = Menu.objects.create(title="Chicken", price=100, inventory=10)
        item = Menu.objects.create(title="Cheese", price=20, inventory=200)
    
    def test_getall(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)