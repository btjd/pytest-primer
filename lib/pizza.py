class MakePizza(object):
    def __init__(self, size=None, crust=None, toppings=[]):
        self.size = size
        self.crust = crust
        self.toppings = toppings

    def make_pizza(self):
        order = "You have ordered a {} {} crust with".format(self.size, self.crust)
        for topping in self.toppings:
            order += " {}".format(topping)
        return order