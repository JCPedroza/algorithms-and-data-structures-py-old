def bubble_sort(nums: list[float]) -> list[float]:
    """Sorts a list in-place using the Booble Sort approach and recursion.

    Time complexity: O(n^2) for best, worst, average.
    Space complexity: O(n) total O(n) auxiliary? (recursion tree depth?)

    Args:
        nums: A list of numbers.

    Returns:
        The sorted list.
    """

    def swap_through(nums: list[float], offset: int, index: int = 0) -> None:
        if index < len(nums) - 1 - offset:
            if nums[index] > nums[index + 1]:
                nums[index], nums[index + 1] = nums[index + 1], nums[index]
            swap_through(nums, offset, index + 1)

    def loop_through(nums: list[float], loop: int = 0) -> None:
        if loop < len(nums) - 1:
            swap_through(nums, loop)
            loop_through(nums, loop + 1)

    loop_through(nums)
    return nums


algorithm = bubble_sort
name = "recursive"
