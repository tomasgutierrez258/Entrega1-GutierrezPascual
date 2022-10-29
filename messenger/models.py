from django.db import models
from django.db import models
# Create your models here.

class Message(models.Model):
    message = models.CharField(max_length = 500)
    sent_by = models.CharField(max_length = 300)
    received_by = models.CharField(max_length = 300)
    
    def __str__(self):
        return self.message, self.sent_by, self.received_by