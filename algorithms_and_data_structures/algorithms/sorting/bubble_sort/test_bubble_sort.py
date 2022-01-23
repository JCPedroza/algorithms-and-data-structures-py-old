from . import bubble_sort
from . import bubble_sort_optimized
from . import bubble_sort_recursive

test_subjects = [
    bubble_sort,
    bubble_sort_optimized,
    bubble_sort_recursive
]


def test_bubble_sort(test_all_subjects):
    test_all_subjects(test_subjects)
