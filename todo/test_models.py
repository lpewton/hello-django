from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_false(self):
        item = Item.objects.create(name='Test To-Do Item')
        self.assertFalse(item.done)

    def test_item_str_method_returns_name(self):
        Item.objects.create(name='Test To-Do-Item')
        self.assertEqual(str(Item), 'Test To-Do Item')
