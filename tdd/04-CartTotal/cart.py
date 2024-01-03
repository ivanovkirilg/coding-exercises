from dataclasses import dataclass, field

@dataclass
class Product:
    price: float
    discounts: "list[float]" = field(default_factory=list)

@dataclass
class Coupon:
    value: float


def _sum_coupons(coupons: "list[Coupon]"):
    return sum(coupon.value for coupon in coupons)

def _get_discounted_price(product):
    price = product.price
    for discount in product.discounts:
        price *= (1.0 - discount)
    return price

def calculate_total(products, coupons: "list[Coupon]" = []):
    discounted_prices = ( _get_discounted_price(product)
                         for product in products )

    total = sum(discounted_prices)

    total -= _sum_coupons(coupons)

    if total < 0:
        total = Coupon(-total)

    return total
