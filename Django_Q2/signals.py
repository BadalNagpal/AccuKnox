import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel


@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, **kwargs):
    print(f"Receiver Thread ID: {threading.get_ident()}")
    print(f"Saved instance: {instance}")