import pytest

class TestCmdOpt(object):
    def test_cmd_opt(self, cmdopt):
        if cmdopt == "cat":
            print("\nMeow Meow")
        elif cmdopt == "dog":
            print("\nWoof Woof")
        assert True