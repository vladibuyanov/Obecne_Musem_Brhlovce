from django.test import TestCase
from django.urls import reverse

from app.models import UserPost


class TestIndexView(TestCase):
    """ Testing index view """

    def test_get(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')


class TestHistoryView(TestCase):
    """ Testing history view """

    def test_get(self):
        response = self.client.get(reverse('history'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/history.html')


class TestImpressionView(TestCase):
    """ Testing impression view """

    def test_get(self):
        response = self.client.get(reverse('impression'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/impression.html')


class TestAddImpressionView(TestCase):
    """ Testing add impression view """

    def test_get(self):
        response = self.client.get(reverse('add_impression'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/add_impression.html')

    def test_post(self):
        """ Testing POST method """
        data = {'name': 'Test User', 'post': 'test post'}
        response = self.client.post(reverse('add_impression'), data=data)
        self.assertEqual(response.status_code, 302)

        queryset = UserPost.objects.filter(name=data['name'], post=data['post'])
        self.assertEqual(queryset.count(), 1)

        expected_queryset = ['Post of Test User']
        self.assertQuerysetEqual(queryset, expected_queryset, transform=str)
