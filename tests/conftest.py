from lib.num_gen import NumGen, GenResults
from lib.pizza import MakePizza
from random import randint
import ast
import pytest

@pytest.fixture(scope='function')
def gen_rand_input():
    return randint(10, 100)

@pytest.fixture(scope='class')
def gen_obj():
    gen_obj = NumGen()
    return gen_obj

@pytest.fixture(scope='class')
def result_obj():
    result_obj = GenResults()
    return result_obj

@pytest.fixture(scope='function')
def pizza_obj():
    pizza_obj = MakePizza()
    return pizza_obj

@pytest.fixture(scope='function')
def testdata_dict(testdata):
        testdata_dictionary = ast.literal_eval(testdata)
        return testdata_dictionary

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")