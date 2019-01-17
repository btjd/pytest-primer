from lib.pizza import MakePizza
import pytest

class TestData(object):
    def test_testdata(self, testdata_dict, pizza_obj):
        pizza_obj.size = testdata_dict['size']
        pizza_obj.crust = testdata_dict['crust']
        pizza_obj.toppings = testdata_dict['toppings']
        order = pizza_obj.make_pizza()
        print(order)
        assert isinstance(pizza_obj, MakePizza)