from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def setUp(self):
        self.item = Menu.objects.create(title="IceCream", price=80)
        
    def test_get_item(self):
        self.assertEqual(self.item.title, "IceCream: 80")