def test_is_valid():
    assert is_valid("1") == True
    assert is_valid("0") == True
    assert is_valid("-1") == False
    assert is_valid("uno") == False
    assert is_valid("u1") == False
    assert is_valid("") == False