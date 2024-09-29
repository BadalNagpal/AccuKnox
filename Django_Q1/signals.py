from django.dispatch import receiver
from .models import my_signal

@receiver(my_signal)
def my_signal_receiver(sender, instance, **kwargs):
    print("Signal received. Processing started.")

    #A time consuming task
    import time
    time.sleep(2)

    print("Signal Processing Completed")