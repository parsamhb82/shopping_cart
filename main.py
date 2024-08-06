from market import *
from product import *
from user import *

market = Market()
user = User()
while (True) :
    inp = input("1- add a product\n2- search for a product\n3- watch your cart\n")
    
    if inp == '1' :
        product_name = input(" enter the product name: ")
        market.add_product(product_name)
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
            pass
    elif inp == '3':
        users_product_list = user.get_product()
        for product in users_product_list :
            product : Product
            print(product.name_getter() , product.price_getter(), product.category_getter, product.score_getter())
        
        cart_inp = input('what do you want to do?\n1- add score to a product\n 2- remove a product\n3- finalize your cart\nelse- nothing go back')
        if cart_inp == '1':
            product_name = input('enter the products name : ')
            product_in_scoring = user.search_in_cart(product_name)
            if product_in_scoring :
                users_score = int(input('enter a number between 1-5'))
                product_in_scoring.add_num_scorers(users_score)
            else :
                print('product is not in your cart ')

        elif cart_inp == '2':
            product_name = input('enter the products name : ')
            product_to_remove = user.search_in_cart(product_name)
            if product_to_remove:
                user.clear_product(product)
            else:
                print('product is not in your cart ')

                
        elif cart_inp == '3':
            for product in users_product_list:
                product : Product
                product.update_stock()
    else :
        print('wrong input number')
