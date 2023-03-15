from urllib import response
from django.test import TestCase
from .models import Item

# Create your tests here.

    class TestViews(TestCase):

        def test_get_todo_list(self):
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'todo/todo_list.html')
            
        def test_get_add_item_page(self):
            response = self.client.get('/add')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'todo/add_item.html')
        
        def test_get_add_item_page(self):
            item - Item.objects.create(name='test todo Item')
            response = self.client.get('/edit/99')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'todo/edit_item.html')
