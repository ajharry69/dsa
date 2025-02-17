from django.db.models import F
from django.http import JsonResponse

from jambo.apps.products.models import Product


def _products_purchasable_within_budget(budget, products):
    purchasable_products = {}
    other_purchasable_products = {}

    remaining_budget = budget

    maximum_purchasable_product_name = ""

    for (name, price, quantity, total_price) in products:
        if total_price <= remaining_budget:
            purchasable_products[name] = quantity
            remaining_budget -= total_price

            if remaining_budget == 0:
                break
        else:
            # here we are asking ourselves how many X dollar products can we buy
            # with the remaining budget?
            purchasable_quantity = min(int(remaining_budget // price), quantity)

            if purchasable_quantity == 0:
                continue

            other_purchasable_products[name] = (purchasable_quantity, price)

            if not maximum_purchasable_product_name or purchasable_quantity > \
                    other_purchasable_products[maximum_purchasable_product_name][0]:
                maximum_purchasable_product_name = name

    while len(other_purchasable_products) > 0 and remaining_budget > 0:
        quantity, price = other_purchasable_products.pop(maximum_purchasable_product_name)
        purchasable_products[maximum_purchasable_product_name] = quantity
        remaining_budget -= (quantity * price)

        for name, quantity_price in other_purchasable_products.copy().items():
            quantity, price = quantity_price
            purchasable_quantity = min(int(remaining_budget // price), quantity)

            if purchasable_quantity == 0:
                del other_purchasable_products[name]
                continue

            other_purchasable_products[name] = (purchasable_quantity, price)

            if not maximum_purchasable_product_name or purchasable_quantity > \
                    other_purchasable_products[maximum_purchasable_product_name][0]:
                maximum_purchasable_product_name = name

    return {
        "remaining_budget": remaining_budget,
        "purchasable_products": purchasable_products,
    }


def products_purchasable_within_budget(request):
    if request.method != 'GET':
        return JsonResponse(
            status=405,
            data={"error": f"Invalid request method. Expect 'GET' but got '{request.method}'."},
        )

    try:
        budget = float(request.GET["budget"])
    except (ValueError, KeyError) as _:
        return JsonResponse(status=404, data={"error": "Service requires a 'budget' as a query parameter"})

    products = (
        Product.objects.annotate(total_price=F("price") * F("quantity"))
        .order_by("quantity", "-price")
        .values_list("name", "price", "quantity", "total_price")
    )
    data = _products_purchasable_within_budget(
        budget=budget,
        products=products,
    )
    return JsonResponse(data=data)
