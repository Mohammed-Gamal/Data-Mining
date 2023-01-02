# Method 1
import statistics
med = statistics.median([1, 2, 3, 4, 5])
print(f'mean is {med}')


# Method 2
def median(nums):
  nums.sort()
  n = len(nums)
  m = n // 2  # floor division

  if n % 2 == 0:
    return (nums[m - 1] + nums[m]) / 2
  else:
    return nums[m]

print(f'mean is {median([1, 2, 3, 4, 5])}')
