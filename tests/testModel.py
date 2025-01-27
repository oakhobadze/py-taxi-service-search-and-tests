from django.test import TestCase

from taxi.models import Manufacturer, Driver, Car


# Create your tests here.
class TestModel(TestCase):
    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(name="test_name", country="test_country")
        self.assertEqual(str(manufacturer), f"{manufacturer.name} {manufacturer.country}")

