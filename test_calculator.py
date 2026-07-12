"""
Tests for calculator.py

Run locally with:  pytest test_calculator.py -v
"""

from calculator import add, subtract, multiply


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-5, -5) == -10
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-1, -1) == 0
    assert subtract(10, 10) == 0

def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(0, 5) == 0
    assert multiply(5, 5) == 25
    assert multiply(10, 10) == 100
    assert multiply(2, 10) == 200
    
