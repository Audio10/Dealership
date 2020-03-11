from django.db import models

""" Vehicle Model """
class Make(models.Model):
    name = models.CharField(unique=True ,max_length=255)
    country = models.CharField(max_length=255)

    
    def __str__(self):
        """Return the Vehicle model."""
        return self.name
