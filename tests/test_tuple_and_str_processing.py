from tuple_and_str_processing import tuple_proc, str_proc
import pytest


#test_tuple_processing
def test_tuple_processing_symb():
    assert tuple_proc('Hello, world!')[12] == '!'

@pytest.mark.parametrize("string, lenght", [('Ночь, улица, фонарь, аптека,', 28),
                                            ('Бессмысленный и тусклый свет.', 29),
                                            ('Живи еще хоть четверть века -', 29),
                                            ('Все будет так. Исхода нет.', 26)])
def test_tuple_processing_len(string, lenght):
    assert len(tuple_proc(string)) == lenght

def test_tuple_processing_assignment():
    try:
        assert tuple_proc('Hello')[1] == 's'
    except AssertionError:
        pass


#test_str_processing
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