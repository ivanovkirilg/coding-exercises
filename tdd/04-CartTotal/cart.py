from dataclasses import dataclass

@dataclass
class Product:
    price: float

@dataclass
class Coupon:
    value: float


def calculate_total(products, coupon=Coupon(0.0)):
    total = sum( prod.price for prod in products )
    reduced_total = total - coupon.value
    return reduced_total
