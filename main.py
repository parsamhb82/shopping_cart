from market import *
from product import *
from user import *
import pickle

user = User()
with open('products.pkl', 'rb') as file:
    products_list = pickle.load(file)
# with open('users_products.pkl', 'rb') as f:
#     user.set_product(pickle.load(f))
    

market = Market(products_list)
while (True) :
    inp = input("1- add a product\n2- search for a product\n3- watch your cart\nelse - close program")
    
    if inp == '1' :
        product_name = input("enter the product name: ")
        users_add_product = market.search_by_name(product_name)
        if users_add_product:
            user.add_product_user(users_add_product)
        else:
            print('product not in the market')
    elif inp == '2':
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
            star_price = int(input("star_price: "))
            end_price = int(input("end_price: "))
            products_list = market.search_by_range(star_price,end_price)
            if products_list == [] :
                print('no match found') 
            else:
                for product in products_list:
                    print(product.name_getter())
    elif inp == '3':
        users_product_list = user.get_product()
        for product in users_product_list :
            product : Product
            print(product.name_getter() , product.price_getter(), product.category_getter(), product.score_getter())
        
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
        print('program closing')
        # with open('users_products.pkl', 'rb') as file:
        #     pickle.dump(user.get_product, file)
        with open('products.pkl', 'rb') as f:
            pickle.dump(products_list, f)


