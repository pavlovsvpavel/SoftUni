from typing import List, Optional

from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Optional[Product]:
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str) -> None:
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)

    def __repr__(self):
        result = []

        for p in self.products:
            result.append(f"{p.name}: {p.quantity}")

        return "\n".join(result)

