'''
Given an array of integers sorted in non-decreasing order, return a new array containing the squares of each number sorted in non-decreasing order.

Examples:

[-3, -2, 0, 4, 6] -> [0, 4, 9, 16, 36]      
[-5, -3, 2, 3, 10] -> [4, 9, 9, 25, 100]

For a fully efficient solution (and full credit), this must be done in O(n) time!


'''
#using counting sort algorithm 
def sort_squares(nums):
    max_value = max(nums)
    print('max_value',max_value)
    bucket = [0]*((max_value**2)+1)
    print('bucket is',bucket)
    for num in nums:
        sqr = num ** 2
        print('sqr is',sqr)
        bucket[sqr] += 1
    final_result = []
    for i in range(len(bucket)):
        i_count = bucket[i]
        for count in range(i_count):
            final_result += [i]
    return final_result 
print(sort_squares([-3, -2, 0, 4, 6]))
print(sort_squares([-5, -3, 2, 3, 10]))


print("=======")
print("optimized solution")

def sort_squares1(nums):
  #edge case
  if len(nums) == 0:
    return nums
  sorted_square_nums = []  # sc = O(len(nums))
  left, right = 0, len(nums) - 1  #two pointers
  while left <= right:  # O(n)
    if abs(nums[left]) >= abs(nums[right]):
      square_value = nums[left]**2
      sorted_square_nums.append(square_value)  # O(1)
      left += 1
    else:
      square_value = nums[right]**2
      sorted_square_nums.append(square_value)  # O(1)
      right -= 1
  return reverse_numbers(sorted_square_nums)


def reverse_numbers(nums):
  if len(nums) == 0 or len(nums) == 1:
    return nums
  left, right = 0, len(nums) - 1
  while left <= right:
    nums[left], nums[right] = nums[right], nums[left]  # reversing
    left += 1
    right -= 1
  return nums


nums = [-3, -2, 0, 4, 6]
nums1 = [0, 3, 6]
nums3 = []
nums4 = [-9, 8, -7, 6]
nums5=[6]
print(sort_squares1(nums))
print(sort_squares1(nums1))
print(sort_squares1(nums3))
print(sort_squares1(nums4))
print(sort_squares1(nums5))
        