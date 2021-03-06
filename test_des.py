from nose.tools import *

from des import * 

class TestDES():

  def setUp(self):
    self.key = "0001001100110100010101110111100110011011101111001101111111110001"

  # move to utils test
  def _test_permutates_key(self):
    given_key = "0001001100110100010101110111100110011011101111001101111111110001"
    expected = "11110000110011001010101011110101010101100110011110001111"
    assert_equals(expected, DES(given_key).key)

  def test_build_first_subkey(self):
    des = DES(self.key)
    expected = "000110110000001011101111111111000111000001110010"

    assert_equals(expected, des.subkeys[0])

  def test_build_second_subkey(self):
    des = DES(self.key)
    expected = "011110011010111011011001110110111100100111100101"

    assert_equals(expected, des.subkeys[1])

  def test_builds_unpermutated_keys(self):
    des = DES(self.key)
    prev_key = "11110000110011001010101011110101010101100110011110001111"
    expected = "11100001100110010101010111111010101011001100111100011110"

    result = des.build_subkey(prev_key, 0)
    assert_equals(expected, result)

  def test_generate_unpermutated_subkeys_for_key(self):
    des = DES(self.key)
    assert_equals(16, len(des.subkeys))
 
  def test_encode_full_message(self):
    message = "0000000100100011010001010110011110001001101010111100110111101111"
    expected = "1000010111101000000100110101010000001111000010101011010000000101"

    des = DES(self.key)
    result = des.encrypt(message)
    assert_equals(expected, result)

  def test_encode_message(self):
    left_zero = "11001100000000001100110011111111"
    right_zero = "11110000101010101111000010101010"
    expected = "0000101001001100110110011001010101000011010000100011001000110100"

    des = DES(self.key)
    message = des.encode(left_zero, right_zero)
    assert_equals(expected, message)

  def test_feistel(self):
    right_zero = "11110000101010101111000010101010"
    expected = "00100011010010101010100110111011"

    des = DES(self.key)
    result = des.feistel(right_zero, 0) 
    assert_equals(expected, result)
  



