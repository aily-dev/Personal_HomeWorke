from django.http import JsonResponse


def get_products(request):
    products = [
        {
            "id": 1,
            "name": "iPhone 15",
            "price": 50000,
            "category": "mobile"
        },
        {
            "id": 2,
            "name": "MacBook Air",
            "price": 80000,
            "category": "laptop"
        },
        {
            "id": 3,
            "name": "AirPods Pro",
            "price": 15000,
            "category": "audio"
        }
    ]

    return JsonResponse({
        "products": products
    })
