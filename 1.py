a = {}
x=0
i=0

while (x!=6):
    print("\nShopping Cart\n1. Add a product to the cart\n2. Search for a product\n3. Delete a product from the cart\n4. Display the contents of the cart\n5. Purchase items\n6. Quit")

    x = int(input("Enter your choice: "))

    if x == 1:
   
        if i < 5:
            y = input("Enter product name: ")
            z = input("Enter product price: ")
            brand = input("Enter product brand: ")
            a[y] = {"price": z, "brand": brand}
            i += 1
            print("Product added to the cart")
        else:
            print("Cart is full")
    elif x == 2:
        search = input("Search for a product: ")
        if search in a:
            print(f"Found: {a[search]}")
        else:
            print("No product exists with this name")
    elif x == 3:
        h=input("delete product from the cart")
        info={"product":" Add a product to the cart","search":" Search for a product","del":"Delete a product from the cart"}
        info.popitem()
        print(info)
    elif x == 4:
        j=input("disply the content from a cart")
        if not a:
            print("Cart is empty")
        else:
            print("Contents of the cart:")
            for product, details in a.items():
                print(f"{product}: {details}")
    


    
   

