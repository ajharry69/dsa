from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from tests.factories import (
    BusinessCategoryFactory,
    BusinessLocationFactory,
    CustomerContactFactory,
    BusinessFactory,
    CustomerFactory,
)


class TestBusinessCategoryViewSet(APITestCase):
    def test_create(self):
        response = self.client.post(
            reverse("businesscategory-list"),
            data={
                "name": "Example",
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        data = response.data
        assert "url" in data
        assert "id" in data
        assert data["name"] == "Example"

    def test_update(self):
        category = BusinessCategoryFactory(name="Example")

        response = self.client.put(
            reverse("businesscategory-detail", kwargs={"pk": category.pk}),
            data={
                "name": "Updated example",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert "url" in data
        assert "id" in data
        assert data["name"] == "Updated example"

    def test_delete(self):
        category = BusinessCategoryFactory()

        response = self.client.delete(
            reverse("businesscategory-detail", kwargs={"pk": category.pk}),
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.data is None

    def test_get_one(self):
        category = BusinessCategoryFactory(name="Example")

        response = self.client.get(
            reverse("businesscategory-detail", kwargs={"pk": category.pk}),
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert "url" in data
        assert "id" in data
        assert data["name"] == "Example"

    def test_get_all(self):
        BusinessCategoryFactory(name="Example")
        BusinessCategoryFactory(name="Example 2")

        response = self.client.get(
            reverse("businesscategory-list"),
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert len(data) == 2


class TestBusinessLocationViewSet(APITestCase):
    def test_create(self):
        response = self.client.post(
            reverse("businesslocation-list"),
            data={
                "county": "Kisumu",
                "sub_county": "Ahero",
                "ward": "Nyando",
                "building_name": "Whitehouse",
                "floor": "2nd",
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        data = response.data
        assert "url" in data
        assert "id" in data
        assert data["county"] == "Kisumu"
        assert data["sub_county"] == "Ahero"
        assert data["ward"] == "Nyando"
        assert data["building_name"] == "Whitehouse"
        assert data["floor"] == "2nd"

    def test_update(self):
        category = BusinessLocationFactory(county="Kisumu")

        response = self.client.put(
            reverse("businesslocation-detail", kwargs={"pk": category.pk}),
            data={
                "county": "Nakuru",
                "sub_county": "Ahero",
                "ward": "Nyando",
                "building_name": "Blackhouse",
                "floor": "3rd",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert "url" in data
        assert "id" in data
        assert data["county"] == "Nakuru"
        assert data["sub_county"] == "Ahero"
        assert data["ward"] == "Nyando"
        assert data["building_name"] == "Blackhouse"
        assert data["floor"] == "3rd"

    def test_delete(self):
        category = BusinessLocationFactory()

        response = self.client.delete(
            reverse("businesslocation-detail", kwargs={"pk": category.pk}),
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.data is None

    def test_get_one(self):
        category = BusinessLocationFactory()

        response = self.client.get(
            reverse("businesslocation-detail", kwargs={"pk": category.pk}),
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert "url" in data
        assert "id" in data
        assert data["county"] == "Nairobi"
        assert data["sub_county"] == "Westlands"
        assert data["ward"] == "Mountain View"
        assert data["building_name"] == "Riverside Flats"
        assert data["floor"] == "4th"

    def test_get_all(self):
        BusinessLocationFactory(county="Nairobi")
        BusinessLocationFactory(county="Nakuru")

        response = self.client.get(
            reverse("businesslocation-list"),
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert len(data) == 2


class TestBusinessViewSet(APITestCase):
    def test_create(self):
        response = self.client.post(
            reverse("business-list"),
            data={
                "name": "JM Pay",
                "registration_date": "2020-09-14",
                "location": {
                    "county": "Kisumu",
                    "sub_county": "Ahero",
                    "ward": "Nyando",
                    "building_name": "Whitehouse",
                    "floor": "2nd",
                },
                "categories": [
                    {
                        "name": "Fintech"
                    },
                ],
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        data = response.data
        assert "url" in data
        assert "id" in data
        assert data["name"] == "JM Pay"
        assert data["registration_date"] == "2020-09-14"
        assert data["location"]["county"] == "Kisumu"
        assert data["location"]["sub_county"] == "Ahero"
        assert data["location"]["ward"] == "Nyando"
        assert data["location"]["building_name"] == "Whitehouse"
        assert data["location"]["floor"] == "2nd"
        assert len(data["categories"]) == 1

    def test_update(self):
        category = BusinessFactory(name="Sweepers")

        response = self.client.put(
            reverse("business-detail", kwargs={"pk": category.pk}),
            data={
                "name": "JM Pay",
                "registration_date": "2020-09-19",
                "location": {
                    "county": "Nakuru",
                    "sub_county": "Ahero",
                    "ward": "Nyando",
                    "building_name": "Whitehouse",
                    "floor": "3rd",
                },
                "categories": [
                    {
                        "name": "Fintech"
                    },
                    {
                        "name": "Transportation"
                    },
                ],
            },
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert "url" in data
        assert "id" in data
        assert data["name"] == "JM Pay"
        assert data["registration_date"] == "2020-09-19"
        assert data["location"]["county"] == "Nakuru"
        assert data["location"]["sub_county"] == "Ahero"
        assert data["location"]["ward"] == "Nyando"
        assert data["location"]["building_name"] == "Whitehouse"
        assert data["location"]["floor"] == "3rd"
        assert len(data["categories"]) == 2

    def test_delete(self):
        category = BusinessFactory()

        response = self.client.delete(
            reverse("business-detail", kwargs={"pk": category.pk}),
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.data is None

    def test_get_one(self):
        category = BusinessFactory()

        response = self.client.get(
            reverse("business-detail", kwargs={"pk": category.pk}),
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert "url" in data
        assert "id" in data

    def test_get_all(self):
        BusinessFactory(name="Nairobi")
        BusinessFactory(name="Nakuru")

        response = self.client.get(
            reverse("business-list"),
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert len(data) == 2


class TestCustomerContactViewSet(APITestCase):
    def test_create(self):
        response = self.client.post(
            reverse("customercontact-list"),
            data={
                "phone": "+254712345678",
                "email": "customer@mail.com",
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        data = response.data
        assert "url" in data
        assert "id" in data
        assert data["phone"] == "+254712345678"
        assert data["email"] == "customer@mail.com"

    def test_update(self):
        category = CustomerContactFactory(phone="+254712345678")

        response = self.client.put(
            reverse("customercontact-detail", kwargs={"pk": category.pk}),
            data={
                "phone": "+254712345679",
                "email": "customer.updated@mail.com",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert "url" in data
        assert "id" in data
        assert data["phone"] == "+254712345679"
        assert data["email"] == "customer.updated@mail.com"

    def test_delete(self):
        category = CustomerContactFactory()

        response = self.client.delete(
            reverse("customercontact-detail", kwargs={"pk": category.pk}),
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.data is None

    def test_get_one(self):
        category = CustomerContactFactory(
            phone="+254712345678",
            email="customer@mail.com",
        )

        response = self.client.get(
            reverse("customercontact-detail", kwargs={"pk": category.pk}),
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert "url" in data
        assert "id" in data
        assert data["phone"] == "+254712345678"
        assert data["email"] == "customer@mail.com"

    def test_get_all(self):
        CustomerContactFactory(phone="+254712345678")
        CustomerContactFactory(phone="+254701234567")

        response = self.client.get(
            reverse("customercontact-list"),
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert len(data) == 2


class TestCustomerViewSet(APITestCase):
    def test_create(self):
        response = self.client.post(
            reverse("customer-list"),
            data={
                "name": "Jack Jill",
                "date_of_birth": "2000-09-14",
                "contact": {
                    "phone": "+254712345678",
                    "email": "customer@mail.com",
                },
                "businesses": [
                    {
                        "name": "JM Pay",
                        "registration_date": "2020-09-14",
                        "location": {
                            "county": "Kisumu",
                            "sub_county": "Ahero",
                            "ward": "Nyando",
                            "building_name": "Whitehouse",
                            "floor": "2nd",
                        },
                        "categories": [
                            {
                                "name": "Fintech"
                            },
                        ],
                    },
                ],
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        data = response.data
        assert "url" in data
        assert "id" in data
        assert data["name"] == "Jack Jill"
        assert data["date_of_birth"] == "2000-09-14"
        assert "url" in data["contact"]
        assert "id" in data["contact"]
        assert data["contact"]["phone"] == "+254712345678"
        assert data["contact"]["email"] == "customer@mail.com"
        assert len(data["businesses"]) == 1

    def test_update(self):
        customer = CustomerFactory(name="James Bond", date_of_birth="2000-11-14")

        response = self.client.put(
            reverse("customer-detail", kwargs={"pk": customer.pk}),
            data={
                "name": "James Bond",
                "date_of_birth": "2000-11-14",
                "contact": {
                    "phone": "+254701234567",
                    "email": "james.bond@mail.com",
                },
                "businesses": [
                    {
                        "name": "JM Pay",
                        "registration_date": "2020-09-19",
                        "location": {
                            "county": "Nakuru",
                            "sub_county": "Ahero",
                            "ward": "Nyando",
                            "building_name": "West End",
                            "floor": "3rd",
                        },
                        "categories": [
                            {
                                "name": "Fintech"
                            },
                            {
                                "name": "Transportation"
                            },
                        ],
                    },
                    {
                        "name": "JM School",
                        "registration_date": "2018-01-14",
                        "location": {
                            "county": "Kisumu",
                            "sub_county": "Ahero",
                            "ward": "Nyando",
                            "building_name": "Whitehouse",
                            "floor": "2nd",
                        },
                        "categories": [
                            {
                                "name": "Learning Institutions"
                            },
                        ],
                    },
                ],
            },
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert "url" in data
        assert "id" in data
        assert data["name"] == "James Bond"
        assert data["date_of_birth"] == "2000-11-14"
        assert "url" in data["contact"]
        assert "id" in data["contact"]
        assert data["contact"]["phone"] == "+254701234567"
        assert data["contact"]["email"] == "james.bond@mail.com"
        assert len(data["businesses"]) == 2

    def test_delete(self):
        customer = CustomerFactory()

        response = self.client.delete(
            reverse("customer-detail", kwargs={"pk": customer.pk}),
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.data is None

    def test_get_one(self):
        customer = CustomerFactory()

        response = self.client.get(
            reverse("customer-detail", kwargs={"pk": customer.pk}),
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert "url" in data
        assert "id" in data
        assert "url" in data["contact"]
        assert "id" in data["contact"]

    def test_get_all(self):
        CustomerFactory(name="John Doe")
        CustomerFactory(name="Jack Jill")

        response = self.client.get(
            reverse("customer-list"),
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert len(data) == 2
