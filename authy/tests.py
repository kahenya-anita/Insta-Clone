from django.test import TestCase
from .models import Profile
class Profile(TestCase):
    def test_fields(self):
        item = item()
        item.user = 'AlfredKe'
        item.first_name = "ALfred"
        item.last_name = "Warui"
        item.location = "Nairobi"
        item.profile_info = "A striving success"
        item.save()

        record = item.objects.get(pk1)
        self.assertEqual(record, item)