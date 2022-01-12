def bubble_sort(nums: list[float]) -> list[float]:
    """Sorts a list in-place using the Bubble Sort approach.

    Time complexity: best O(n) worst O(n^2) average O(n^2)
    Space complexity: total O(n) auxiliary O(1)

    Args:
        nums: A list of numbers.

    Returns:
        The sorted list.
    """

    for round in range(len(nums) - 1):
      sorted = True

      for index in range(len(nums) - 1 - round):
        if nums[index] > nums[index + 1]:
          nums[index], nums[index + 1] = nums[index + 1], nums[index]
          sorted = False

      if sorted: break

    return nums

algorithm = bubble_sort
id = 'optimized'
