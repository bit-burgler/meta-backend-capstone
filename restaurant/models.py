from django.db import models

class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    
class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField()
    booking_date = models.DateField()
    
    def __str__(self):
        return f'{self.name} for {self.number_of_guests} guests on {self.booking_date}'
    
