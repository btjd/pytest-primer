import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="cat", help="my option: cat or dog"
    ),
    parser.addoption(
        "--testdata", action="append", help="dict to pass to test functions"
    )

def pytest_generate_tests(metafunc):
    if 'testdata' in metafunc.fixturenames:
        metafunc.parametrize("testdata", metafunc.config.getoption('testdata'))
    
