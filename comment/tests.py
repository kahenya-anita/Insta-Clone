from django.test import TestCase
from .models import  Comment
class Comment(TestCase):
    def test_fields(self):
        item = item()
        item.user = 'Alfred'
        item.post = "Football"
        item.date = "10/19/moday"
        item.body = "We're the football team your mother warned you about."
        item.save()

        record = item.objects.get(pk1)
        self.assertEqual(record, item)
