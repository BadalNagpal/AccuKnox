from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Author, Book

@receiver(post_save, sender=Author)
def create_book(sender, instance, created, **kwargs):
    if created:
        Book.objects.create(title=f"Book by {instance.name}", author=instance)