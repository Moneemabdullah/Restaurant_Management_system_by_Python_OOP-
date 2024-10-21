class Order:
    def __init__(self):
        self.items = {}

    def add_item(self,item):
        if item in self.items:
            self.items[item] += item.quantity#jodi item cart a thake 
        else:
            self.items[item] += item.quantity#jodi age na thake

    def remove_item(self ,item):
        if item in self.items:
            del self.items[item]

    @property
    def total_prize(self):
        return sum(item.price * quantity for item, quantity in self.items.items())

    def clear(self):
        self.items  = {}


