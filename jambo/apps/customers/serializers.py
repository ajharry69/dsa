from django.db.transaction import atomic
from rest_framework import serializers

from jambo.apps.customers import models


class BusinessCategorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.BusinessCategory
        fields = "__all__"


class BusinessLocationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.BusinessLocation
        fields = "__all__"


class BusinessSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    age_in_days = serializers.IntegerField(read_only=True)
    location = BusinessLocationSerializer()
    categories = BusinessCategorySerializer(many=True)

    class Meta:
        model = models.Business
        fields = "__all__"

    def _save_categories(self, value):
        categories = []
        errors = []
        for data in value:
            serializer = BusinessCategorySerializer(data=data)
            if not serializer.is_valid(raise_exception=False):
                errors.append(serializer.errors)
                continue

            category = models.BusinessCategory.objects.get_or_create(**serializer.validated_data)[0]
            categories.append(category)
        if errors:
            raise serializers.ValidationError(errors)
        return categories

    def _save_location(self, value):
        serializer = BusinessLocationSerializer(data=value)
        if serializer.is_valid(raise_exception=False):
            return models.BusinessLocation.objects.get_or_create(
                **serializer.validated_data,
            )[0]
        raise serializers.ValidationError(serializer.errors)

    @atomic
    def create(self, validated_data):
        location = self._save_location(validated_data.pop("location"))
        categories = self._save_categories(validated_data.pop("categories"))
        business = super().create(validated_data={"location": location, **validated_data})
        business.categories.set(categories)
        return business

    @atomic
    def update(self, instance, validated_data):
        location = self._save_location(validated_data.pop("location"))
        categories = self._save_categories(validated_data.pop("categories"))
        business = super().update(
            instance=instance,
            validated_data={"location": location, **validated_data},
        )
        business.categories.set(categories)
        return business


class CustomerContactSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.CustomerContact
        fields = "__all__"


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    contact = CustomerContactSerializer()
    businesses = BusinessSerializer(many=True)
    businesses_url = serializers.HyperlinkedRelatedField(view_name="businesses", read_only=True)

    class Meta:
        model = models.Customer
        fields = "__all__"

    def _save_businesses(self, value):
        businesses = []
        errors = []
        for data in value:
            serializer = BusinessSerializer(data=data)
            if not serializer.is_valid(raise_exception=False):
                errors.append(serializer.errors)
                continue

            business = serializer.save()
            businesses.append(business)
        if errors:
            raise serializers.ValidationError(errors)
        return businesses

    def _save_contact(self, value):
        serializer = CustomerContactSerializer(data=value)
        if serializer.is_valid(raise_exception=False):
            return models.CustomerContact.objects.get_or_create(
                **serializer.validated_data,
            )[0]
        raise serializers.ValidationError(serializer.errors)

    @atomic
    def create(self, validated_data):
        contact = self._save_contact(validated_data.pop("contact"))
        businesses = self._save_businesses(validated_data.pop("businesses"))
        customer = super().create(validated_data={"contact": contact, **validated_data})
        customer.businesses.set(businesses)
        return customer

    @atomic
    def update(self, instance, validated_data):
        contact = self._save_contact(validated_data.pop("contact"))
        businesses = self._save_businesses(validated_data.pop("businesses"))
        customer = super().update(
            instance=instance,
            validated_data={"contact": contact, **validated_data},
        )
        customer.businesses.set(businesses)
        return customer
