'''
Given an array, reorder the elements such that

a[0] <= a[1] >= a[2] <= a[3]…

There may be more than one valid result, just output any possible result.

Example
[1, 2, 3, 4, 5] -> [1, 3, 2, 5, 4]  
    
[1, 2, 3, 2, 1] -> [1, 2, 1, 3, 2]

You must do this in O(nlogn) time.

(You can actually do this in O(n) time)

'''

def wiggleSort(nums: list[int]) -> None:
  def isEven(num):
    return num % 2 == 0

  for i in range(0, len(nums)-1): # o(n)
    if isEven(i) and nums[i] > nums[i+1]:
      nums[i], nums[i+1] = nums[i+1], nums[i]
    elif not isEven(i) and nums[i] < nums[i+1]:
      nums[i], nums[i+1] = nums[i+1], nums[i]
  return nums 
nums = [1,2,3,4,5]
print(wiggleSort(nums))

print("doing in  nlogn time ")


