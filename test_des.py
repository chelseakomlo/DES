from nose.tools import *

from des import * 

class TestDES():

  def setUp(self):
    self.key = "0001001100110100010101110111100110011011101111001101111111110001"

  def test_permutates_key(self):
    given_key = "0001001100110100010101110111100110011011101111001101111111110001"
    expected = "11110000110011001010101011110101010101100110011110001111"
    assert_equals(expected, DES(given_key).key)

  def test_build_first_subkey(self):
    des = DES(self.key)
    expected = "000110110000001011101111111111000111000001110010"
    initial_key = permutate(self.key, PC1)
    subkeys = des.gen_subkeys()

    assert_equals(expected, subkeys[0])

  def test_build_second_subkey(self):
    des = DES(self.key)
    prev_key = "000110110000001011101111111111000111000001110010"
    expected = "011110011010111011011001110110111100100111100101"
    subkeys = des.gen_subkeys()

    assert_equals(expected, subkeys[1])

  def test_builds_unpermutated_keys(self):
    des = DES(self.key)
    prev_key = "11110000110011001010101011110101010101100110011110001111"
    expected = "11100001100110010101010111111010101011001100111100011110"

    result = des.build_subkey(prev_key, 0)
    assert_equals(expected, result)

  def test_generate_unpermutated_subkeys_for_key(self):
    des = DES(self.key)

    subkeys = des.build(self.key)
    assert_equals(16, len(subkeys))

