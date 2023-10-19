from pykur.funcs.fun_compose import compose
from math import pow

def test1():
    assert compose(max, pow)(5, 6) == 15625.0