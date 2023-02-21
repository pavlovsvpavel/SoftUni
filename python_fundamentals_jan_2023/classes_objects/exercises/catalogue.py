class Catalogue:
    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        specific_products = [x for x in self.products if x.startswith(first_letter)]
        return specific_products

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        result += "\n".join(sorted(self.products))
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
