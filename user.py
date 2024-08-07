from product import Product
class User:
    def __init__(self):
        self.__product = []
    def add_product_user(self, product):
        self.__product.append(product)
        
    def clear_product(self, product):
        self.__product.remove(product)
        
    def get_product(self):
        return self.__product

    def search_in_cart(self, product_name):
        for product in self.__product:
            product : Product
            if product_name == product.name_getter():
                return product
        return None
    
    def set_product(self, product_list):
        self.__product = product_list


