class market:
    def __init__ (self, product_list : list) :
        if product_list :
            self.__product_list = product_list
        else:
            product_list = []

    def search_by_name(self, product_name):
        pass
        
        #return product
    
    def search_by_range(self, star_price, end_price):
        pass

    def search_by_category(self, category_name):
        pass

    def add_product(self, product):
        self.__product_list.append(product)
    
    def product_list_getter(self):
        return self.__product_list()

