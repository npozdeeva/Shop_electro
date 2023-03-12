class Product:
    product_all = []
    pay_rate = 0.85

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        self.product_all.append(self)

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def calculate_total_price(self):
        self.total_price = self.price * self.count


item1 = Product("Смартфон", 10000, 20)
item2 = Product("Ноутбук", 20000, 5)



print(item1.price)
item1.apply_discount()
print(item1.price)
print(item2.price)

print(Product.product_all)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
