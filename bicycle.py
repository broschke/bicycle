####incomplete#####

class Bicycle(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
    

class Shop(object):
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
        self.profit = 0
        
    def sell(self, model):
        found = None
        for i in self.inventory:
            if i.model == model:
                found = i
        self.inventory.remove(found)
        
        self.profit += 0.2 * found.cost
        return found
    
    def show_profit(self):
        print ()
        
class Customer(object):
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.own = []
        
    def buy(self, bought_bike):
        pass
    
    def owned_bike(self):
        if self.own == []:
            return False
        else:
            return True
    
    

bike1 = Bicycle("mountain", 14, 500)
bike2 = Bicycle("bmx", 11, 400)
bike3 = Bicycle("street", 12, 350)

store1 = Shop("bikes r us", [bike1, bike2, bike3])
sold_bike = store1.sell("bmx") 
print(store1.profit)
print(store1.inventory)
bob = Customer("bob", 1000)
bob.buy(sold_bike)
