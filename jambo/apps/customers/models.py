import datetime

from django.core import validators
from django.db import models


def past_date_validator(dob):
    today = datetime.date.today()
    if dob > today:
        raise validators.ValidationError(f"Date cannot be after than {today}")


class BusinessCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Business category"
        verbose_name_plural = "Business categories"

    def __str__(self):
        return self.name


class BusinessLocation(models.Model):
    county = models.CharField(max_length=100, db_index=True)
    sub_county = models.CharField(max_length=150, db_index=True)
    ward = models.CharField(max_length=150, db_index=True)
    building_name = models.CharField(max_length=200, db_index=True)
    floor = models.CharField(max_length=50, db_index=True)

    class Meta:
        verbose_name = "Business location"
        verbose_name_plural = "Business locations"
        unique_together = (
            ("county", "sub_county", "ward", "building_name", "floor"),
        )

    def __str__(self):
        return f"{self.county}, {self.sub_county}, {self.ward}, {self.building_name}, {self.floor}"


class Business(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    registration_date = models.DateField(validators=(past_date_validator,), db_index=True)
    categories = models.ManyToManyField("customers.BusinessCategory", related_name="categories")
    location = models.ForeignKey("customers.BusinessLocation", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Business"
        verbose_name_plural = "Businesses"

    def __str__(self):
        return f"{self.name}, {self.location}"

    @property
    def age_in_days(self):
        age = datetime.date.today() - self.registration_date
        return age.days


class CustomerContact(models.Model):
    phone = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Customer contact"
        verbose_name_plural = "Customer contacts"
        unique_together = (
            ("phone", "email"),
        )

    def __str__(self):
        return f"{self.email} ({self.phone})"


class Customer(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    contact = models.OneToOneField("customers.CustomerContact", on_delete=models.CASCADE)
    date_of_birth = models.DateField(validators=(past_date_validator,), db_index=True)
    nationality = models.CharField(max_length=100, db_index=True)
    businesses = models.ManyToManyField("customers.Business")

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name
