def bubble_sort(nums: list[float]) -> list[float]:
    """Sorts a list in-place using the Bubble Sort approach.

    Time complexity: O(n^2) forst best, worst, average
    Space complexity: total O(n) auxiliary O(1)

    Args:
        nums: A list of numbers.

    Returns:
        The sorted list.
    """

    for _ in range(len(nums)):
      for index in range(len(nums) - 1):
        if nums[index] > nums[index + 1]:
          nums[index], nums[index + 1] = nums[index + 1], nums[index]

    return nums

algorithm = bubble_sort
id = 'simple'
