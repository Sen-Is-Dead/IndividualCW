from django.db import models

class MyModel(models.Model):
    """
    Model representing an instance with various field types.
    """
    char_field = models.CharField(max_length=100)
    date_field = models.DateField()
    email_field = models.EmailField()
    integer_field = models.IntegerField()
