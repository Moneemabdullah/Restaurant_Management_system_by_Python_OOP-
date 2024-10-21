from abc import ABC
from orders import Order

class user(ABC):
    def __init__(self, name, phone, email,address):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone


class Customar(user):
    def __init__(self, name, phone, email, address):
        super.__init__(name, phone, email, address)
        self.cart = Order()

    def view_manu(self, resturent):
        resturent.manu.show_manue()

    def add_to_cart(self,resturent, item_name, quantity):
        item = resturent.manue.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("item quantity exceeded!!")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("item added")
        else:
            print('Item not found')

    def view_cart(self):
        print("********view cart********")
        print("Name:\tPrice\tQuentity")
        for item,quantity in self.cart.items():
            print(f'{item.name}\t{item.price}\t{item.quantity}')
        print('total price: {self.cart.total_price}')

    def pay_bil(self):
        print(f'Total {self.cart.total_prize} paid sucessfully')
        self.cart.clear()


class Employee(user):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super.__init__(name, phone, email, address)
        self.age  = age
        self.designation = designation
        self.salary = salary

    
class Admin(user):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurent,employee):
        restaurent.add_employee(employee)

    
    def view_employee(self,rasturent,):
        rasturent.view_employee()

    def add_new_item(self,resturent, item):
        resturent.manu.add_manue_item(item)

    def remove_item(self,resturent, item):
        resturent.manu.remove_item(item)

    def view_menu(self,rasturent):
        rasturent.menu.show_menu() 






        
