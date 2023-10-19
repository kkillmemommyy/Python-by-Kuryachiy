from pykur.loops.cube_sum import cube_sum


def test1():
    assert cube_sum(87539319) == 3

def test2():
    assert cube_sum(4) == 0

def test3():
    assert cube_sum(16) == 1