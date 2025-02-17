from django.urls import path

from jambo.apps.products.views import products_purchasable_within_budget

app_name = "products"
urlpatterns = [
    path("products", view=products_purchasable_within_budget, name="budget-products"),
]
