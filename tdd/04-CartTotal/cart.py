from dataclasses import dataclass

@dataclass
class Product:
    price: float


def calculate_total(products, coupon=0.0):
    return sum( prod.price for prod in products ) - coupon
