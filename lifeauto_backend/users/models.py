from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    country_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)

    nationality = models.CharField(max_length=100)
    languages = models.JSONField()
    date_of_birth = models.DateField()

    street = models.CharField(max_length=255) 
    floor_number = models.CharField(max_length=20, blank=True, null=True)  
    postcode = models.CharField(max_length=20)
    city = models.CharField(max_length=100)

    has_bank_account = models.BooleanField()
    bank_account_number = models.CharField(max_length=34, blank=True, null=True)

    is_student = models.BooleanField()
    is_over_26 = models.BooleanField()
    has_company = models.BooleanField()

    apps = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"