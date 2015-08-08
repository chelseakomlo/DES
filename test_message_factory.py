from nose.tools import *

from message_factory import *

class TestMessageFactory():

  def test_substitute(self):
    message = "011000010001011110111010100001100110010100100111"
    factory = MessageFactory(message)

    expected = "01011100100000101011010110010111"
    factory.substitute()
    assert_equals(expected, factory.message)

  def test_sbox(self):
    block = "011011"
    expected = "0101"

    factory = MessageFactory("some message")
    actual = factory.sbox(block, 0)
    assert_equals(expected, actual)

  def test_xor_no_change(self):
    message = "01"
    key  = "00"
    expected = "01"

    factory = MessageFactory(message)
    actual = factory.xor(key)
    assert_equals(expected, factory.message)


