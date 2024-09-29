from django.db import models
from django.dispatch import Signal
import time

#custom-signal
my_signal = Signal()

class MyModel(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        print("Model Save Started")
        
        #Demonstration Time
        start_time = time.time()

        #continue with the actual save
        super().save(*args, **kwargs)

        #Trigger the Signal
        my_signal.send(sender=self.__class__, instance=self)

        print("Signal Handling Completed")
        print(f"Total Time taken for save: {time.time() - start_time} seconds")