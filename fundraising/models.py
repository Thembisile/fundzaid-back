from django.db import models

class Campaign(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='')
    goal = models.DecimalField(max_digits=10, decimal_places=2)

class Fundraiser(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount_fundraised = models.DecimalField(max_digits=10, decimal_places=2) 
    goal = models.DecimalField(max_digits=10, decimal_places=2) 
    description = models.TextField(default='')

