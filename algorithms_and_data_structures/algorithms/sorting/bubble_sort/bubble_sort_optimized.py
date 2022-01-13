def bubble_sort(nums: list[float]) -> list[float]:
    """Sorts a list in-place using the Bubble Sort approach.

    Time complexity: best O(n) worst O(n^2) average O(n^2).
    Space complexity: total O(n) auxiliary O(1).

    Args:
        nums: A list of numbers.

    Returns:
        The sorted list.
    """

    for loop in range(len(nums) - 1):
        is_sorted = True

        for index in range(len(nums) - 1 - loop):
            if nums[index] > nums[index + 1]:
                nums[index], nums[index + 1] = nums[index + 1], nums[index]
                is_sorted = False

        if is_sorted:
            break

    return nums


algorithm = bubble_sort
name = 'optimized'
