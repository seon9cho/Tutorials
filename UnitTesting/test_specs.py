# test_specs.py
"""Python Essentials: Unit Testing.
<Name>
<Class>
<Date>
"""

import specs
import pytest


def test_add():
    assert specs.add(1, 3) == 4, "failed on positive integers"
    assert specs.add(-5, -7) == -12, "failed on negative integers"
    assert specs.add(-6, 14) == 8

def test_divide():
    assert specs.divide(4,2) == 2, "integer division"
    assert specs.divide(5,4) == 1.25, "float division"
    with pytest.raises(ZeroDivisionError) as excinfo:
        specs.divide(4, 0)
    assert excinfo.value.args[0] == "second input cannot be zero"


# Problem 1: write a unit test for specs.smallest_factor(), then correct it.
def test_smallest_factor():
    assert specs.smallest_factor(1) == 1, "failed on base case n = 1"
    assert specs.smallest_factor(2) == 2, "failed on base case n = 2"
    assert specs.smallest_factor(3) == 3, "failed on base case n = 3"
    assert specs.smallest_factor(4) == 2, "failed on composition n = 4 = 2*2"
    assert specs.smallest_factor(5) == 5, "failed on base case n = 5"
    assert specs.smallest_factor(6) == 2, "failed on composition n = 6 = 3*2"
    assert specs.smallest_factor(10) == 2, "failed on composition n = 10 = 5*2"
    assert specs.smallest_factor(15) == 3, "failed on composition n = 15 = 5*3"
    assert specs.smallest_factor(99) == 3, "failed on large number n = 99"
    assert specs.smallest_factor(169) == 13, "failed on perfect square n = 169 = 13**2"
    assert specs.smallest_factor(1073) == 29, "failed on prime composition n = 1073 = 29*37"

# Problem 2: write a unit test for specs.month_length().
def test_month_length():
    assert specs.month_length(5) == None, "failed for invalid input"
    assert specs.month_length("April") == 30, "failed on April for set of months with 30 days"
    assert specs.month_length("August") == 31, "failed on August for set of months with 31 days"
    assert specs.month_length("February") == 28, "failed on February for non leap year"
    assert specs.month_length("February", leap_year=True) == 29, "failed on February for leap year"

# Problem 3: write a unit test for specs.operate().
def test_operate():
    assert specs.operate(4, 5, '+') == 9, "failed for '+' operator"
    assert specs.operate(3, 6, '-') == -3, "failed for '-' operator"
    assert specs.operate(6, -7, '*') == -42, "failed for '*' operator"
    assert specs.operate(15, 3, '/') == 5, "failed for '/' operator"
    with pytest.raises(TypeError) as excinfo_1:
        specs.operate(14, 2, 5)
    assert excinfo_1.value.args[0] == "oper must be a string"
    with pytest.raises(ZeroDivisionError) as excinfo_2:
        specs.operate(4, 0, '/')
    assert excinfo_2.value.args[0] == "division by zero is undefined"
    with pytest.raises(ValueError) as excinfo_3:
        specs.operate(3, 2, '=')
    assert excinfo_3.value.args[0] == "oper must be one of '+', '/', '-', or '*'"


# Problem 4: write unit tests for specs.Fraction, then correct it.
@pytest.fixture
def set_up_fractions():
    frac_1_3 = specs.Fraction(1, 3)
    frac_1_2 = specs.Fraction(1, 2)
    frac_n2_3 = specs.Fraction(-2, 3)
    return frac_1_3, frac_1_2, frac_n2_3

def test_fraction_init(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_3.numer == 1
    assert frac_1_2.denom == 2
    assert frac_n2_3.numer == -2
    frac = specs.Fraction(30, 42)
    assert frac.numer == 5
    assert frac.denom == 7
    with pytest.raises(ZeroDivisionError) as excinfo_1:
        specs.Fraction(1, 0)
    assert excinfo_1.value.args[0] == "denominator cannot be zero"
    with pytest.raises(TypeError) as excinfo_1:
        specs.Fraction('3', '5')
    assert excinfo_1.value.args[0] == "numerator and denominator must be integers"

def test_fraction_str(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert str(frac_1_3) == "1/3"
    assert str(frac_1_2) == "1/2"
    assert str(frac_n2_3) == "-2/3"
    frac = specs.Fraction(30, 5)
    assert str(frac) == '6'

def test_fraction_float(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert float(frac_1_3) == 1 / 3.
    assert float(frac_1_2) == .5
    assert float(frac_n2_3) == -2 / 3.

def test_fraction_eq(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_2 == specs.Fraction(1, 2)
    assert frac_1_3 == specs.Fraction(2, 6)
    assert frac_n2_3 == specs.Fraction(8, -12)
    assert specs.Fraction(3, 5) == 0.6

def test_fraction_add(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_2 + frac_1_3 == specs.Fraction(5, 6)
    assert frac_1_3 + frac_n2_3 == specs.Fraction(-1, 3)

def test_fraction_sub(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_2 - frac_1_3 == specs.Fraction(1, 6)
    assert frac_1_3 - frac_n2_3 == specs.Fraction(1, 1)

def test_fraction_mul(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_2 * frac_1_3 == specs.Fraction(1, 6)
    assert frac_1_3 * frac_n2_3 == specs.Fraction(-2, 9)

def test_fraction_truediv(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_2 / frac_1_3 == specs.Fraction(3, 2)
    assert frac_1_3 / frac_n2_3 == specs.Fraction(-1, 2)
    with pytest.raises(ZeroDivisionError) as excinfo:
        frac_1_3 / specs.Fraction(0, 3)
    assert excinfo.value.args[0] == "cannot divide by zero"

# Problem 5: Write test cases for Set.
def test_count_sets():
    hand1 = ["1022", "1122", "0100", "2021",
            "0010", "2201", "2111", "0020",
            "1102", "0200", "2110", "1020"]
    assert specs.count_sets(hand1) == 6
    hand2 = hand1.copy()
    hand2.remove("1020")
    with pytest.raises(ValueError) as excinfo_1:
        specs.count_sets(hand2)
    assert excinfo_1.value.args[0] == "there are not exactly 12 cards"
    hand3 = hand1.copy()
    hand3[11] = "2110"
    with pytest.raises(ValueError) as excinfo_2:
        specs.count_sets(hand3)
    assert excinfo_2.value.args[0] == "the cards are not all unique"
    hand4 = hand1.copy()
    hand4[11] = "10201"
    with pytest.raises(ValueError) as excinfo_3:
        specs.count_sets(hand4)
    assert excinfo_3.value.args[0] == "one or more cards does not have exactly 4 digits"
    hand5 = hand1.copy()
    hand5[11] = "1420"
    with pytest.raises(ValueError) as excinfo_4:
        specs.count_sets(hand5)
    assert excinfo_4.value.args[0] == "one or more cards has a character other than 0, 1, or 2"

def test_is_set():
    hand1 = ["1022", "1122", "0100", "2021",
            "0010", "2201", "2111", "0020",
            "1102", "0200", "2110", "1020"]
    assert specs.is_set(hand1[0], hand1[3], hand1[7]) == True
    assert specs.is_set(hand1[3], hand1[6], hand1[5]) == True
    assert specs.is_set(hand1[11], hand1[10], hand1[9]) == True
    assert specs.is_set(hand1[1], hand1[6], hand1[2]) == True
    assert specs.is_set(hand1[0], hand1[6], hand1[9]) == True
    assert specs.is_set(hand1[1], hand1[4], hand1[5]) == True
    assert specs.is_set(hand1[1], hand1[2], hand1[3]) == False



