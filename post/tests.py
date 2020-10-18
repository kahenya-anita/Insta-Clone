from django.test import TestCase
from .models import Post, Follow, Stream, Likes
class Post(TestCase):
    def test_fields(self):
        item = item()
        item.caption = 'Yummy'
        item.posted = "10/19/moday"
        item.tags = "Foodie"
        item.user = "Alfred"
        item.likes= "20"
        item.save()

        record = item.objects.get(pk1)
        self.assertEqual(record, item)

class Follow(TestCase):
    def test_fields(self):
        item = item()
        item.follower = 'Tatiana, Rose, Clavis'
        item.following = "Claudia, Mark"
        
        item.save()

        record = item.objects.get(pk1)
        self.assertEqual(record, item)

class Stream(TestCase):
    def test_fields(self):
        item = item()
        item.following = "Claudia, Mark"
        item.user = "Alfred"
        item.post = "Image of a Burger"
        item.date = "10/19/moday"
        item.save()

        record = item.objects.get(pk1)
        self.assertEqual(record, item)

class Likes(TestCase):
    def test_fields(self):
        item = item()
        item.user = "Rose"
        item.post = "Image of a Burger"
        item.save()

        record = item.objects.get(pk1)
        self.assertEqual(record, item)


