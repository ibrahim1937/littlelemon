from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_items(self):
        item = Menu.objects.create(Title="Test Item", Inventory=10, Price=10.0)
        self.assertEqual(str(item), "Test Item : 10.0")