from django.test import TestCase
from django.test.client import Client
from authapp.models import CustomUser
from django.core.management import call_command


class TestUserManagement(TestCase):
    def setUp(self):
        call_command('flush','--noinput')
        call_command('loaddata','test_db.json')
        self.client = Client()

        self.superuser = CustomUser.objects.create_superuser('django2','django@mango.gr','geek')
        self.user = CustomUser.objects.create_user('testuser','test@mail.ru','somepassword')
        self.user_with_first_name = CustomUser.objects.create_user('holmes','hos@en.en','holmes',first_name='Sherlock')


    def test_user_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertTrue(response.context['user'].is_anonymous)

        self.client.login(username='testuser',password='somepassword')

        response = self.client.get('/auth/login')
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(response.context['user'], self.user)

        response = self.client.get('/')
        self.assertContains(response, 'User', status_code=200)
        self.assertEqual(response.context['user'], self.user)

    def test_user_logout(self):
        self.client.login(username='testuser',password='somepassword')
        response = self.client.get('/auth/login/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_anonymous)
        response = self.client.get('/auth/logout/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)

    def tearDown(self):
        call_command('sqlsequencereset','mainapp','authapp', 'ordersapp', 'basketapp')


# Create your tests here.
