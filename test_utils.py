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

  def test_lshift_shifts_two(self):
    block = "1234"

    result = lshift(block, 2)
    assert_equals("3412", result)

  def test_split(self):
    block = [1, 2, 3, 4]
    left, right = split(block)

    assert_equals([1, 2], left)
    assert_equals([3, 4], right)

