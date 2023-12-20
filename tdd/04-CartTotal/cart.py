from dataclasses import dataclass

@dataclass
class Product:
    price: float
    discount: float = 0.0

@dataclass
class Coupon:
    value: float


def _sum_coupons(coupons: "list[Coupon]"):
    return sum(coupon.value for coupon in coupons)

def _get_discounted_price(product):
    return product.price * (1.0 - product.discount)

def calculate_total(products, coupons: "list[Coupon]" = []):
    total = sum( _get_discounted_price(prod) for prod in products )

    total -= _sum_coupons(coupons)

    if total < 0:
        return Coupon(-total)
    return total
