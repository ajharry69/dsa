from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from jambo.apps.customers import serializers, models
from jambo.mixins import PaginatedResponseModelViewSetMixin


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


class CustomerViewSet(PaginatedResponseModelViewSetMixin, ModelViewSet):
    serializer_class = serializers.CustomerSerializer
    queryset = models.Customer.objects.select_related(
        "contact",
    ).prefetch_related(
        "businesses",
        "businesses__location",
        "businesses__categories",
    )

    @extend_schema(responses=serializers.BusinessSerializer(many=True))
    @action(
        detail=True,
        url_path="businesses",
        serializer_class=serializers.BusinessSerializer,
    )
    def get_businesses(self, request, *args, **kwargs):
        queryset = self.get_object().businesses.select_related(
            "location",
        ).prefetch_related("categories")
        return self.paginate_response(queryset)
