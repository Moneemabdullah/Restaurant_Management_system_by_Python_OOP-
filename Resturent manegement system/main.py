from food_item import FoodItem
from manu import Manu
from user import Customar, Admin, Employee
from restaurent import Resturent
from orders import Order

mamar_resturent = Resturent("Mamar Resturent")


def customar_manu():
    name = input("enter your name: ")
    email = input("Enter your Email: ")
    phone = input("enter your phone: ")
    address = input("Enter your address: ")

    customar = Customar(name = name, email = email, phone = phone, address = address)

    while True:
        print(f'Welcome {customar.name}!!')
        print('1. View menu')
        print('2. Add item to cart')
        print('3. View Cart')
        print('4. Pay bil')
        print('5. Exit')

        coice  = int(input("Enter your coice: "))

        if coice == 1:
            customar.view_manu(mamar_resturent)
        elif coice == 2:
            item_name = input("Enter item name: ")
            item_quantity = int(input('enter item quantity'))
            customar.add_to_cart(mamar_resturent,item_name,item_quantity)
        elif coice == 3:
            customar.view_cart()
        elif coice == 4:
            customar.pay_bil()
        elif coice == 5:
            break
        else:
            print("Invalide input")

def admin_manu():
    name = input("enter your name: ")
    email = input("Enter your Email: ")
    phone = input("enter your phone: ")
    address = input("Enter your address: ")

    admin = Admin(name = name, email = email, phone = phone, address = address)

    while True:
        print(f'Welcome {admin.name}!!')
        print('1. Add new item')
        print('2. Add new Employee')
        print('3. View Employee')
        print('4. View Items')
        print('5. Deleat Item')
        print('6. exit')

        coice  = int(input("Enter your coice: "))

        if coice == 1:
            item_name = input("Enter item name: ")
            item_price =  int(input("Enter item prize: "))
            item_quantity = int(input('enter item quantity'))

            item = FoodItem(item_name,item_price,item_quantity) 
            admin.add_new_item(mamar_resturent,item)

        elif coice == 2:
            employee_name = input("Enter Employee name: ")
            employee_phone = input("Enter phone: ")
            employee_email = input("Enter email: ")
            employee_address = input("Enter address: ")
            employee_age = int(input("Enter age: "))
            employee_desuignaion = input("Enter designation: ")
            employee_salary = int(input("Enter age: "))
            new_employee = Employee(employee_name,employee_phone,employee_email,
                                    employee_address,employee_age,employee_desuignaion,employee_salary)
            admin.add_employee(mamar_resturent,new_employee)
        elif coice == 3:
            admin.view_employee(mamar_resturent)
        elif coice == 4:
            admin.view_menu(mamar_resturent)
        elif coice == 5:
            item_name = input("Enter item name: ")
            admin.remove_item(mamar_resturent, item_name)
        elif coice == 6:
            break
        else:
            print("Invalide input")
        

while True:
    print('welcome')
    print('1. customar')
    print('2. admin')
    print('3. Exit')

    coice = int(input("enter your choice: "))
    if coice == 1:
        customar_manu()
    elif coice == 2:
        admin_manu()
    elif coice == 3:
        print("thank You")
        break
    else:
        print("Invalid coice")

