from . import insertion_sort

test_subjects = [
    insertion_sort
]


def test_bubble_sort(test_all_subjects):
    test_all_subjects(test_subjects)
