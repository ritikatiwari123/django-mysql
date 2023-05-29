from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=250, help_text="It store the company_name")
    city = models.CharField(max_length=100, help_text="It store the city in which company is established")
    is_active = models.BooleanField(default=True, help_text="it tells that company still exist/active")

    class Meta:
        db_table = 'company'



