from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import transaction
from .models import Author, Book

class Transactiontest(TestCase):
    def test_transaction(self):
        with self.assertRaises(ValidationError):
            with transaction.atomic():
                author = Author(name='John Doe')
                author.save()                       #triggers the post_save signal
                raise ValidationError("Simulating an error to trigger rollback")
            
        #Verify that no books were created
        self.assertEqual(Book.objects.count(), 0)