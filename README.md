## Sample commands to experiment with the code in this repository:

----
**The files involved in the following commands are:**

   - `pytest-primer/lib/num_gen.py`
   - `pytest-primer/tests/conftest.py`
   - `pytest-primer/tests/test_num_gen.py`

> Omits console output generated by the test
    
    [/tests]$ pytest test_num_gen.py

> The -s option prints messages generated by the test
    
    [/tests]$ pytest -s test_num_gen.py

> Runs all tests within a test class

    [/tests]$ pytest -s test_num_gen.py::TestNumGen 

> Runs a specific method within a test class

    [/tests]$ pytest -s test_num_gen.py::TestNumGen::test_gen_odds
    [/tests]$ pytest -s test_num_gen.py::TestNumGen::test_gen_evens
    [/tests]$ pytest -s test_num_gen.py::TestNumGen::test_gen_squares
> Runs only tests specified with markers

    [/tests]$ pytest -s test_num_gen.py -m odds
    [/tests]$ pytest -s test_num_gen.py -m evens
    [/tests]$ pytest -s test_num_gen.py -m squares

----
**The files involved in the following commands are:**

   - `pytest-primer/conftest.py`
   - `pytest-primer/tests/conftest.py`
   - `pytest-primer/tests/test_cmd_opt.py`
   
> Runs a test that uses the default command option value as a test input
    
    [/tests]$ pytest -s test_cmd_opt.py

> Runs a test that uses a string input to a command loption as a test input

    [/tests]$ pytest -s test_cmd_opt.py --cmdopt='dog'
    [/tests]$ pytest -s test_cmd_opt.py --cmdopt='cat'

----
**The files involved in the following command are:**

   - `pytest-primer/lib/pizza.py`
   - `pytest-primer/conftest.py`
   - `pytest-primer/tests/conftest.py`
   - `pytest-primer/tests/test_testdata.py`

> Runs a test that uses test input data in json format

    [/tests]$ pytest test_testdata.py -s --testdata="{'size':'large', 'crust':'thin', 'toppings':['sausage', 'peppers', 'onions']}"

**Finally, here are the related links to topics covered from the official py.test documentation:**

1) Directory layout best practices
[https://docs.pytest.org/en/latest/goodpractices.html](https://docs.pytest.org/en/latest/goodpractices.html)

2) File organization and fixtures
[https://docs.pytest.org/en/latest/fixture.html](https://docs.pytest.org/en/latest/fixture.html)

3) markers and test execution
[https://docs.pytest.org/en/latest/example/markers.html](https://docs.pytest.org/en/latest/example/markers.html)
[https://docs.pytest.org/en/latest/usage.html](https://docs.pytest.org/en/latest/usage.html)

4) Passing command line options
[https://docs.pytest.org/en/latest/example/simple.html](https://docs.pytest.org/en/latest/example/simple.html)

5) Parametizing tests using cli options
[https://docs.pytest.org/en/latest/example/parametrize.html](https://docs.pytest.org/en/latest/example/parametrize.html)
[https://docs.pytest.org/en/latest/parametrize.html](https://docs.pytest.org/en/latest/parametrize.html)