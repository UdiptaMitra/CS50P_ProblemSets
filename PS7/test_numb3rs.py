from numb3rs import validate


def test_valid():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("192.168.1.1") == True
    assert validate("127.0.0.1") == True


def test_invalid_numbers():
    assert validate("256.0.0.1") == False
    assert validate("275.3.6.28") == False
    assert validate("999.999.999.999") == False
    assert validate("-1.2.3.4") == False


def test_invalid_format():
    assert validate("1.2.3") == False
    assert validate("hello.world") == False
    assert validate("1234") == False
    assert validate("1..2.3") == False
    assert validate("1.2.3.4.5") == False


def test_invalid_leading_zeros():
    assert validate("000.001.010.100") == False
    assert validate("01.2.3.4") == False
    assert validate("1.02.3.4") == False
    assert validate("1.2.003.4") == False
