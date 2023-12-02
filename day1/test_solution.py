from solution import str_to_int, calculate


def test_str_to_int_if_all_can_be_int():
    text = "ninefourone1"
    assert str_to_int(text) == "9411"


def test_str_to_int_if_one_element_can_be_int():
    text = "53sevenvvqm"
    assert str_to_int(text) == "537vvqm"


def test_str_to_int_if_multiple_elements_can_be_int():
    text = "28gtbkszmrtmnineoneightmx"
    assert str_to_int(text) == "28gtbkszmrtm91ightmx"


def test_calculate_only_one_int():
    text = "ninefourone1"
    assert calculate(text) == 11


def test_calculate_two_int():
    text = "53sevenvvqm"
    assert calculate(text) == 53


def test_calculate_two_int_2():
    text = "72fivebt9ndgq"
    assert calculate(text) == 79
