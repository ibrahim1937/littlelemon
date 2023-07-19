from django.test import TestCase
from restaurant.models import Menu



class MenuViewTest(TestCase):
    # setUp method is called before each test in this class
    def setUp(self):
        Menu.objects.create(Title="Test Item", Inventory=10, Price=10.00)
    
    # Test for correct menu item
    def test_getall(self):
        items = Menu.objects.all()
        self.assertEqual(items[0].Title, "Test Item")
        self.assertEqual(items[0].Inventory, 10)
        self.assertEqual(items[0].Price, 10.00)
        self.assertEqual(len(items), 1)

        
