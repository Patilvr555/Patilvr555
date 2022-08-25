

import os 

while True:
    print("1:Add your item in cart ")
    print("2:remove your item in cart")
    print("3:Shoe cart")
    print("4:Purchase order")
    print("5:Exit")
    

    choice=int(input("enter your choice :"))
    

    cart=[]

    if choice==1:
        item=input("enter your item ")
        cart.append(item)
        print("Cart items=",item)

    elif choice==2:
        reitem=input("enter item you want to remove :")
        print(cart)
        if reitem in cart:
            cart.remove(reitem)
            print(cart)
        else:
            print("you item is not present in cart ")

    elif choice==3:
        print("your items in cart are",cart)

    elif choice==4:
        purorder=input("enter your order :")
        if purorder in cart:
            print("you purchased tthis item ")
        else:
            print("go to choice :1 and add your item to cart")

    else:
        print("Exit")


    