from django.db import models

class Flight(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    tickets = models.IntegerField()
    airline = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.source} to {self.destination} on {self.date} "
    
