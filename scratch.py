import csv
class Product:
    product_all = []
    pay_rate = 0.8

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        self.product_all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', {self.count})"


    def __str__(self):
        return f'{self.name}'


    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def calculate_total_price(self):
        self.total_price = self.price * self.count
        return self.total_price

    @staticmethod
    def is_integer(data):
        if data % 1 == 0:
            return int(data)
        else:
            return float(data)


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) <= 10:
            self.__name = value
        else:
            raise Exception('Длина наименования товара превышает 10 символов')


    @classmethod
    def instantiate_from_csv(cls, filename: str = 'items.csv') -> list:
        items: list = []
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                price = float(row['price'])
                count = int(row['count'])
                row['price'] = int(price) if cls.is_integer(price) else price
                row['count'] = count
                items.append(cls(**row))
        return items


# #task1
# item1 = Product("Смартфон", 10000, 20)
# item2 = Product("Ноутбук", 20000, 5)
#
# print(item1.price)
# item1.apply_discount()
# print(item1.price)
# print(item2.price)
#
# print(Product.product_all)
#
# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
#
# product = Product('Телефон', 10000, 5)
#
# print(product.name)
#
# #product.name = 'СуперСмартфон'
#
#
Product.instantiate_from_csv()  # создание объектов из данных файла
#print(len(Product.product_all))  # в файле 5 записей с данными по товарам
#
product1 = Product.product_all[5]
print(product1.price)
#
#
# print(Product.is_integer(5))
# print(Product.is_integer(5.0))
# print(Product.is_integer(5.5))

item1 = Product("Смартфон", 10000, 20)
# >>> item1
# Item('Смартфон', 10000, 20)
print(item1)
