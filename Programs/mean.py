# Method 1
def mean1(nums):
  mean = sum(nums)/len(nums)
  print(f'mean is {mean}')

mean1([1,2,3,4])


# Method 2
def mean2(nums):
  mean = 0

  for n in nums:
    mean += n

  mean /= len(nums)

  print(f'mean is {mean}')

mean2([1,2,3,4])


# Method 3
import statistics
m = statistics.mean([1,2,3,4])
print(f'mean is {m}')
