from django.urls import reverse
from rest_framework.test import APITestCase


class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('user-register')
        self.login_url = 'api/v1/auth/token/'

        self.user_data = {
            'email': 'admin@admin.com',
            'password': '@Aq123456',
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
