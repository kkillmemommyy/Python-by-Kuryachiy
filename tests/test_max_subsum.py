from pykur.max_subsum import max_subsum


def test_positive1():
    numbs = [1, 2, 3, 4]
    assert max_subsum(numbs) == 10


def test_positive2():
    numbs = [
        2, 3, -7, -1, 3, 
        4, 5, -2, -4, 7,
        8, -6, -1, 0,
    ]
    assert max_subsum(numbs) == 21


def test_positive3():
    numbs = [
        2, 3, -7, -1, 3, 
        4, 5, -2, -4, 7,
        8, -6, -1, 0, 99,
    ]
    assert max_subsum(numbs) == 99


def test_positive3():
    numbs = [
        2, 3, -7, -1, 3, 
        4, 5, -2, -200, 7,
        8, -6, -1, 0, -3,
    ]
    assert max_subsum(numbs) == 15


def test_negative_1():
    numbs = [-1, -2, -1, -13]
    assert max_subsum(numbs) == -1


def test_negative_2():
    numbs = [-10]
    assert max_subsum(numbs) == -10


def test_negative_3():
    numbs = [-9, -17, -5, -2, -7, -12, -8]
    assert max_subsum(numbs) == -2


def test_negative_4():
    numbs = [-9, -17, -5, -5, -7, -12, -3]
    assert max_subsum(numbs) == -3


def test_negative_5():
    numbs = [-9, -17, -5, -5, -3, -3, -3]
    assert max_subsum(numbs) == -3
