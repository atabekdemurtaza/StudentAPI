from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@test.com',
            password='123456',
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title='Sample type of words',
            body='There are several sentences'
        )

    def test_post_model(self):
        self.assertEqual(first=self.post.author.username, second='testuser')
        self.assertEqual(first=self.post.title, second='Sample type of words')
        
