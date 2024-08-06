from market import *
from product import *
from user import *

market = Market()
user = User()
while (True) :
    inp = input("1- add a product\n2- search for a product\n3- watch your cart\n")
    
    if inp == '1' :
        product_name = input("enter the product name: ")
        users_add_product = market.search_by_name(product_name)
        if users_add_product:
            user.add_product(users_add_product)
        else:
            print('product not in the market')
    elif inp == '2 ':
        inp = input("by what do you want to search?\n1 - search by name\n2- search by category\n3 - search by range\n ")
        if inp == '1' :
            product_name = input("enter the product name: ")
            product = market.search_by_name(product_name)
            if product == None:
                print('no match found')
            else :
                print(product_name)
        elif inp =='2':
            category = input("enter the category : ")
            this_category_products = market.search_by_category(category)
            if this_category_products == []:
                print('no match found') 
            else:
                for product in this_category_products:
                    print(product.name_getter())
        elif inp == '3':
            star_price = input("star_price: ")
            end_price = input("end_price: ")
            products_list = market.search_by_range(star_price,end_price)
            if products_list == [] :
                print('no match found') 
            else:
                for product in products_list:
                    print(product.name_getter())

            


        
    else :
        print('wrong input number')
