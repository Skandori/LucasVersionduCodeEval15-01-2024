from Turing import *
import pytest

def test_decomposer():
    assert decomposer(254) == (2, 5, 4)
    assert decomposer(218) == (2, 1, 8)

def test_divisible():
    assert divisible(81) == True
    assert divisible(31) == False

def test_somme():
    assert somme(5, 2, 3) == True
    assert somme(9, 4, 5) == True
    assert somme(5, 5, 4) == False