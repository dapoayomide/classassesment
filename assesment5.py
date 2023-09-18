class InventoryItem:



    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price
    

    def add_quantity(self,amount):
        self.quantity += amount
        return self.quantity

    def remove_quantity(self,amount):
        if amount > self.quantity:
            print('invalid')
        else:
            self.quantity -= amount
            return self.quantity

    def get_total_value(self):
        return self.quantity * self.price
    

inventory = InventoryItem('aston',12,120000)

print(inventory.add_quantity(12))

print(inventory.remove_quantity(1))
print(inventory.get_total_value())
