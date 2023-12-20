from dataclasses import dataclass

@dataclass
class Product:
    price: float

@dataclass
class Coupon:
    value: float


def calculate_total(products, coupons: "list[Coupon]" = []):
    total = sum( prod.price for prod in products )

    reduced_total = total - sum(
        coupon.value for coupon in coupons)

    if reduced_total < 0:
        return Coupon(-reduced_total)
    return reduced_total
