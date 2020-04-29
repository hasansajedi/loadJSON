from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from django.test import Client

from app.views import report


class ViewTest(TestCase):
    def test_call_view_home(self):
        print('******************test_home_page()**********************')
        c = Client()
        if c.login(username='admin', password='qazWSX@123'):
            response = c.get('/')
            self.assertEqual(response.status_code, 200)

    def test_call_view_report(self):
        print('******************test_report_page()**********************')
        # send GET request.
        c = Client()
        if c.login(username='admin', password='qazWSX@123'):  # defined in fixture or with factory in setUp()
            response = self.client.get('/report')
            print('Response status code : ' + str(response.status_code))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'templates/app/report.html')
