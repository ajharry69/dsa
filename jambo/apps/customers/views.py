from rest_framework.viewsets import ModelViewSet

from jambo.apps.customers import serializers, models


class BusinessCategoryViewSet(ModelViewSet):
    serializer_class = serializers.BusinessCategorySerializer
    queryset = models.BusinessCategory.objects.all()


class BusinessLocationViewSet(ModelViewSet):
    serializer_class = serializers.BusinessLocationSerializer
    queryset = models.BusinessLocation.objects.all()


class BusinessViewSet(ModelViewSet):
    serializer_class = serializers.BusinessSerializer
    queryset = models.Business.objects.select_related(
        "location",
    ).prefetch_related("categories")


class CustomerContactViewSet(ModelViewSet):
    serializer_class = serializers.CustomerContactSerializer
    queryset = models.CustomerContact.objects.all()


class CustomerViewSet(ModelViewSet):
    serializer_class = serializers.CustomerSerializer
    queryset = models.Customer.objects.select_related(
        "contact",
    ).prefetch_related(
        "businesses",
        "businesses__location",
        "businesses__categories",
    )
