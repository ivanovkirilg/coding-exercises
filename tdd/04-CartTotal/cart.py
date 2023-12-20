from dataclasses import dataclass

@dataclass
class Product:
    price: float

@dataclass
class Coupon:
    value: float


def _sum_coupons(coupons: "list[Coupon]"):
    return sum(coupon.value for coupon in coupons)

def calculate_total(products, coupons: "list[Coupon]" = []):
    total = sum( prod.price for prod in products )

    total -= _sum_coupons(coupons)

    if total < 0:
        return Coupon(-total)
    return total
