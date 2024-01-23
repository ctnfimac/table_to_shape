from django.test import TestCase
from django.urls import reverse, reverse_lazy


class TablesTest(TestCase):
    url = reverse_lazy('web:tables')

    def test_tables_valid_in_schema_public(self):
        data = {'schema': 'public'}
        url = reverse('web:tables', args=['public'])
        response = self.client.get(url)
        print(response)