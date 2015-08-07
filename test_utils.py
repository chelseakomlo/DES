from nose.tools import *

from des import * 

class TestUtils():

  def test_permutate(self):
    block = "1234" 
    iterator = [3, 2, 1, 0]

    result = permutate(block, iterator)
    assert_equals("4321", result)

  def test_lshift_shifts_one(self):
    block = "1234"

    result = lshift(block, 1)
    assert_equals("2341", result)

  def test_split(self):
    block = [1, 2, 3, 4]
    left, right = split(block)

    assert_equals([1, 2], left)
    assert_equals([3, 4], right)

  def test_xor_no_change(self):
    block1 = "01"
    block2 = "00"
    expected = "01"

    actual = xor(block1, block2)
    assert_equals(expected, actual)

  def test_xor_with_change(self):
    block1 = "01"
    block2 = "10"
    expected = "11"

    actual = xor(block1, block2)
    assert_equals(expected, actual)

  def test_binary_add(self):
    a = "01"
    b = "01"

    result = binary_add(a, b)
    assert_equals('10', result)
