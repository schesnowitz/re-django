from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    address = models.CharField(max_length=150)
    square_footage = models.IntegerField()

    def __str__(self):
        return self.title