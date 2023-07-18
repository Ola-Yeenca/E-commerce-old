from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='core_items')

    def formatted_price(self):
        # Replace 'USD' with the appropriate currency symbol
        return f'{self.price:.2f} EUR'

    def __str__(self):
        return self.name
