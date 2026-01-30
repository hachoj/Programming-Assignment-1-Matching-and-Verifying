import pytest

from assignment1.verifier import is_stable, one_to_one


def test_one_to_one_positive():
    """
    Test a valid one-to-one matching returns True
    """
    match = [1, 2, 3]
    assert one_to_one(match) == True


def test_one_to_one_negative():
    """
    Test an invalid one-to-one matching returns False
    """
    match = [1, 2, 2]
    assert one_to_one(match) == False


def test_is_stable_positive():
    """
    Test a valid stable matching returns True
    """
    hospital_prefs = [[1, 2, 3], [2, 3, 1], [2, 1, 3]]
    student_prefs = [[2, 3, 1], [1, 2, 3], [1, 2, 3]]
    match = [2, 3, 1]
    assert is_stable(hospital_prefs, student_prefs, match) == True


def test_is_stable_negative():
    """
    Test an invalid stable matching returns False
    """
    hospital_prefs = [[1, 2, 3], [2, 3, 1], [2, 1, 3]]
    student_prefs = [[2, 3, 1], [1, 2, 3], [1, 2, 3]]
    match = [2, 1, 3]
    assert is_stable(hospital_prefs, student_prefs, match) == False
