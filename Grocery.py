# Grocery Manger projects

import json
import os 

File = "Grocery.txt"

#load item
def load_items():
    if not  os.path.exists("File"):
        return []
   
    with open("File","r") as f:
        try:
            return json.load(f)
        except:
            return[]
            
#save file data
def save_items(items):
    with open("File","w")as f:
        json.dump(items, f, indent=4)
            
    
#def add item
def add_items():
    item = input("Enter Item:")
    qty = (input("Enter Qty:"))
    price = int(input("Enter Price:"))

    items = load_items()
    items.append({"Item": [item],"Qty": [qty],"Price":[price]})
    save_items(items)

    print("\n ** Added Items Successfully **")


#view Output
def view_items():
    items = load_items()

    if not items:
        print("No Items Found!\n")
        return
        
    print("\n ____ Grocery Items ____")
    for i,item in enumerate(items, start=1):
        print(f"{i}. fItem :{item['Item']} | fQty: {item['Qty']} | fPrice: {item['Price']}")
    print()    

#updat data
def update_items():
    items = load_items()
    view_items()
    
    index = int(input("Enter Item to Update:")) - 1

    if 0 <= index < len(items):
        items[index]['price'] = int(input("Enter New Price: "))
        items[index]['quantity'] = (input("Enter New Quantity: "))
        
        save_items(items)
        print("**Item Updated Successfully**")
    else:
        print("Invalid Item Number")

#delete items
def delete_items():
    items = load_items()
    view_items()

    index = int(input("Enter to Delete Item:")) - 1

    if 0 <= index < len(items):
        items.pop(index)
        save_items(items)
        print("**Item deleted Successfully!**")
    else:
        print("Invalid item number")

#menu function
def menu():
    while True:
        print(" === Welcome Grocery Store === ")
        print("=======  Grocery Management  =======")
        print(f"1.Add Item:")
        print(f"2.View Item:")
        print(f"3.Update Item:")
        print(f"4.Delete Item:")
        print(f"5.Exit:")


        choice=input("Enter Your Choice:")


        if choice == "1":
            add_items()

        elif choice == "2":
            view_items()

        elif choice == "3":
            update_items()

        elif choice == "4":
            delete_items()

        elif choice == "5":
            print("**Thank You**")
            break

        else:
            print("Invalid Choice\n")


#call form menu function\
menu()
        
            
            

        
        
    
