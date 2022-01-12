from . import bubble_sort
from . import bubble_sort_optimized

test_subjects = [
    bubble_sort,
    bubble_sort_optimized
]

def test_bubble_sort(test_all_subjects):
    test_all_subjects(test_subjects)
