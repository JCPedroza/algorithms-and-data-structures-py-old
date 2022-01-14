from . import merge_sort

test_subjects = [
    merge_sort
]


def test_merge_sort(test_all_subjects):
    test_all_subjects(test_subjects)
