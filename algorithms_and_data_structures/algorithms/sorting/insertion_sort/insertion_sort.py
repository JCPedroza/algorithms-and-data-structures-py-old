def insertion_sort(nums: list[float]) -> list[float]:
    """Sorts a list in-place using the Insertion Sort approach.

    Time complexity: best O(n) worst O(n^2) average O(n^2)
    Space complexity: total O(n) auxiliary O(1)

    Args:
        nums: A list of numbers.

    Returns:
        The sorted list.
    """

    for loop in range(1, len(nums)):
        pivot = loop

        while pivot > 0 and nums[pivot - 1] > nums[pivot]:
            nums[pivot - 1], nums[pivot] = nums[pivot], nums[pivot - 1]
            pivot -= 1

    return nums


algorithm = insertion_sort
name = "simple"
