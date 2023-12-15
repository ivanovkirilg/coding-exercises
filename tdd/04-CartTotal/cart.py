from dataclasses import dataclass

@dataclass
class Product:
    price: float


def calculate_total(products, coupon=0.0):
    total = sum( prod.price for prod in products )
    return total - coupon
