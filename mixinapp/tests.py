from django.test import TestCase
from mixinapp.models import Book
from datetime import date

class BookTestCase(TestCase):

    def setUp(self):
        print('Setup activity')
        published_date = date(year=1990, month=8, day=23)
        Book.objects.create(title='The Secret', author='Richard', published_date=published_date)
        published_date = date(year=1980, month=1, day=3)
        Book.objects.create(title='The Story of Malamala', author='Laxmi Kher', published_date=published_date)

    def test_book_info(self):
        print('testing Book Information')
        qs = Book.objects.all()
        print(qs.count())  # Verify the number of books retrieved
        self.assertEqual(qs.count(), 2)
        e1 = Book.objects.get(title='The Secret')
        e2 = Book.objects.get(title='The Story of Malamala')
        self.assertEqual(e1.author, 'Richard')
        self.assertEqual(e2.author, 'Laxmi Kher')

    def tearDown(self):
        print('Tear down activity')
        Book.objects.all().delete()
