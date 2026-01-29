def test_example():
    a = 3
    b = 3
    assert a is b, "a should have the same memory location as b"


def test_example_2():
    a = 3.1
    b = -3.1
    assert a is not b, "a should have a different memory location then b"