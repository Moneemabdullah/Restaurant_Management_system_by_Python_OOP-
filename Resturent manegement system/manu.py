
class Manu:
    def __init__(self):
        self.items = []


    def add_manu_item(self, item):
        self.items.append(item)

    def find_item(self, item):
        for item in self.items:
            if(item.name.lower() == item.name.lower()):
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
        else:
            print(f'Item not found')

    def show_menue(self):
        print("****Manue*****")
        print("name\tPrice\tQuentity")
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')
