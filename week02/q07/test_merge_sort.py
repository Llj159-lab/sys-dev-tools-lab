from merge_sort import merge_sort


def test_given_input():
    data = [3, 1, 4, 1, 5, 9, 2, 6]
    assert merge_sort(data) == [1, 1, 2, 3, 4, 5, 6, 9]


def test_duplicate_elements():
    data = [4, 2, 4, 1, 2, 4]
    assert merge_sort(data) == [1, 2, 2, 4, 4, 4]
