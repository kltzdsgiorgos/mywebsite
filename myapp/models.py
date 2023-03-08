from django.db import models

TAX = 0.24

class Receipt(models.Model):
    issue_date = models.DateTimeField()
    price_per_liter = models.FloatField()
    total_value = models.FloatField()
    
    def __str__(self):
        return "Paid " + str(self.total_value) + " " + "At: " + str(self.price_per_liter) + " per liter"

    @property
    def calculate_tax_value(self):
        tax_value = self.total_value * TAX
        return tax_value

    @property
    def calculate_net_value(self):
        net_value = self.total_value - self.calculate_tax_value
        return net_value
    
    @property
    def calculate_liters(self):
        liters = self.total_value / self.price_per_liter
        return liters
    
    class Meta:
        ordering = ['issue_date']
    
