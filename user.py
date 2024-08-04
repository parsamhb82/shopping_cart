class User:
    def __init__(self):
        self.__product = []
    def add_product_user(self, product):
        self.__product.append(product)
        
    def clear_product(self, product):
        self.__product.remove(product)
        
    def get_product(self):
        return self.__product 

