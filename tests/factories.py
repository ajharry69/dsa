import factory

from jambo.apps.customers import models


class BusinessCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.BusinessCategory
        django_get_or_create = ("name",)

    name = factory.Faker("name")


class BusinessLocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.BusinessLocation
        django_get_or_create = ("county", "sub_county", "ward", "building_name", "floor")

    county = "Nairobi"
    sub_county = "Westlands"
    ward = "Mountain View"
    building_name = "Riverside Flats"
    floor = "4th"


class BusinessFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Business
        django_get_or_create = ("name",)

    name = factory.Faker("company")
    registration_date = factory.Faker("date_of_birth")
    location = factory.SubFactory(BusinessLocationFactory)


class CustomerContactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.CustomerContact
        django_get_or_create = ("email", "phone")

    email = factory.Faker("email")
    phone = factory.Faker("phone_number")


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Customer
        django_get_or_create = ("contact",)

    name = factory.Faker("name")
    nationality = factory.Faker("country")
    contact = factory.SubFactory(CustomerContactFactory)
    date_of_birth = factory.Faker("date_of_birth")
