from product import Product
from user import User
class Market:
    def __init__ (self, product_list : list) :
        if product_list :
            self.__product_list = product_list
        else:
            product_list = []

    def search_by_name(self, product_name):
        for product in self.__product_list:
            if product_name == product.name_getter():
                return product
        return
    
    def search_by_range(self, star_price, end_price):
        result = []
        for product in self.__product_list:
            if product.price_getter() >= star_price and product.price_getter() <= end_price :
                result.append(product)
        return result

    def search_by_category(self, category_name):
        result = []
        for product in self.__product_list:
            if product.category_getter() == category_name:
                result.append(product)
        return result

    def add_product(self, name, price, category, stock, score, num_scorers):
        product = Product(name, price, category, stock, score, num_scorers)
        self.__product_list.append(product)
    
    def product_list_getter(self):
        return self.__product_list()

