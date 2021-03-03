from str_processing import str_proc
import pytest

def test_str_processing_upper():
    assert str_proc("hello").upper() == "HELLO"

@pytest.mark.parametrize("string, substring, index", [("Hello world!", "world", 6),
                                                      ("92233 72036 85477 5807", "85477", 12),
                                                      ("!@# $% ^&* ()_+", "^&*", 7)])
def test_str_processing_index(string, substring, index):
    assert str_proc(string).index(substring) == index

def test_str_processing_strtoint():
    try:
        assert int(str_proc("12+"))
    except ValueError:
        pass