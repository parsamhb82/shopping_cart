class Product:
    def __init__(self,name, price, category, stock, score, num_scorers):
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__category = category
        self.__score = score
        self.__num_scorers = num_scorers

    def add_num_scorers(self, score):
        pass
    
    def update_stock(self):
        pass

    def price_getter(self):
        return self.__price

    def stock_getter(self):
        return  self.__stock 

    def score_getter(self):
        return self.__score
    
    def name_getter(self):
        return  self.__name
    
    def category_getter(self):
        return  self.__category

    def num_scorers_getter(self):
        return  self.__num_scorers


    
