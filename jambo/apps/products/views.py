from django.http import JsonResponse

from jambo.apps.products.models import Product


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

    remaining_budget = budget
    maximum_purchasable_product_name = ""

    purchasable_products = {}
    products = {
        product.name: (product.quantity, product.price)
        for product in Product.objects.all()
    }

    while len(products) > 0 and remaining_budget > 0:
        if maximum_purchasable_product_name:
            quantity, price = products.pop(maximum_purchasable_product_name)
            purchasable_products[maximum_purchasable_product_name] = quantity
            remaining_budget -= (quantity * price)

        for name, quantity_price in products.copy().items():
            quantity, price = quantity_price
            purchasable_quantity = min(int(remaining_budget // price), quantity)

            if purchasable_quantity == 0:
                del products[name]
                continue

            products[name] = (purchasable_quantity, price)

            if not maximum_purchasable_product_name or purchasable_quantity > \
                    products[maximum_purchasable_product_name][0]:
                maximum_purchasable_product_name = name

    return JsonResponse(
        data={
            "remaining_budget": remaining_budget,
            "purchasable_products": purchasable_products,
        },
    )
