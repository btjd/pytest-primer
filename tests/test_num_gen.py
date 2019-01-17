from math import sqrt
import pytest

class TestNumGen(object):
    @pytest.mark.odds
    def test_gen_odds(self, gen_rand_input, gen_obj, result_obj):
        print("\nCurrent random input is: " + str(gen_rand_input))
        result_obj.odds = gen_obj.gen_odds(gen_rand_input)
        print(result_obj.odds)
        assert result_obj.odds == list(range(1, gen_rand_input, 2))

    @pytest.mark.evens
    def test_gen_evens(self, gen_rand_input, gen_obj, result_obj):
        print("\nCurrent random input is: " + str(gen_rand_input))
        result_obj.evens = gen_obj.gen_evens(gen_rand_input)
        print(result_obj.evens)
        assert result_obj.evens == list(range(0, gen_rand_input, 2))

    @pytest.mark.squares
    def test_gen_squares(self, gen_rand_input, gen_obj, result_obj):
        print("\nCurrent random input is: " + str(gen_rand_input))
        result_obj.squares = gen_obj.gen_squares(gen_rand_input)
        print(result_obj.squares)
        assert [sqrt(x) for x in result_obj.squares] == list(range(gen_rand_input))

    def test_return_results(self, result_obj):
        print(result_obj)