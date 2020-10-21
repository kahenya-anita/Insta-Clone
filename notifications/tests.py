from django.test import TestCase
from .models import Notification

class Notification(TestCase):
    def test_fields(self):
        item = item()
        item.user = 'Alfred'
        item.post = "Post"
        item.sender = "Crush"
        item.notification_type = "Comment."
        item.preview = "You look prettier than a picture."
        item.date = "10/19/monday"
        item.is_seen = "False"
        item.save()

        record = item.objects.get(pk1)
        self.assertEqual(record, item)
