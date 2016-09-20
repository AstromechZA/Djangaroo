from django.test import TestCase, RequestFactory, Client
from django.forms.models import model_to_dict

from example_project.apps.example_app.models import Example


class ListExamplesTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_normal_get_empty(self):
        response = self.client.get('/examples/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['examples']), [])

    def test_normal_get_with_items(self):
        e1 = Example.objects.create(name='Sample1')
        e2 = Example.objects.create(name='Sample2')

        response = self.client.get('/examples/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['examples']), [e1, e2])


class NewExampleTest(TestCase):

    def test_post(self):
        e1 = Example(name='Sample1')
        response = self.client.post('/examples/new', model_to_dict(e1))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/examples/1')
