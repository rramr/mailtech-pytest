from tuple_processing import tuple_proc
import pytest

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
