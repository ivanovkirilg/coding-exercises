from dataclasses import dataclass

@dataclass
class Product:
    price: float


def calculate_total(products):
    return sum( prod.price for prod in products )
