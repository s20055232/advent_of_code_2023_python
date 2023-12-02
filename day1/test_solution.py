from solution import str_to_int, calculate, old_calculate


def test_str_to_int_if_all_can_be_int():
    text = "ninefourone1"
    assert str_to_int(text) == {8: 1, 4: 4, 0: 9}


def test_str_to_int_if_one_element_can_be_int():
    text = "53sevenvvqm"
    assert str_to_int(text) == {2: 7}


def test_str_to_int_if_multiple_elements_can_be_int():
    text = "28gtbkszmrtmnineoneightmx"
    assert str_to_int(text) == {12: 9, 16: 1, 18: 8}


def test_old_calculate_only_one_int():
    text = "ninefourone1"
    assert old_calculate(text) == 11


def test_old_calculate_two_int():
    text = "53sevenvvqm"
    assert old_calculate(text) == 53


def test_old_calculate_two_int_2():
    text = "72fivebt9ndgq"
    assert old_calculate(text) == 79


def test_calculate_two_int_2():
    text = "ninefourone1"
    assert calculate(text) == 91


def test_calculate_if_multiple_elements_can_be_int():
    text = "28gtbkszmrtmnineoneightmx"
    assert calculate(text) == 28


def test_calculate_if_one_element_can_be_int():
    text = "53sevenvvqm"
    assert calculate(text) == 57
