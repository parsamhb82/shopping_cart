from market import *
from product import *
from user import *

market = Market()

while (True) :
    inp = input("1- add a product\n2- search for a product\n3- watch your cart\n")
    
    if inp == '1' :
        product_name = input(" enter the product name: ")
        market.add_product(product_name)
    elif inp == '2 ':
        search_inp = input("by what do you want to search?\n1 - search by name\n2- search by category\n3 - search by range\n ")
        if inp == '1' :
            product_name = input("enter the product name: ")
            product = market.search_by_name(product_name)
            if product == None:
                print('no match found')
            else :
                print(product_name)
        elif inp =='2':
            pass
    elif inp == '3':
        pass
    else :
        print('wrong input number')
