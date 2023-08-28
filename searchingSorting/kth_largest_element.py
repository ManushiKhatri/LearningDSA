'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Approach Using Quick Select : 

A selection algorithm to find the k-th smallest or largest element in an unordered set.

The algorithm is similar to QuickSort. The difference is, instead of recursing on both sides (after finding pivot), it recurses only for the part that contains the k-th smallest or largest element. 

The logic is simple, if index of partitioned element is more than k, 
then we recur for left part. 
If index is same as k, we have found the k-th largest element and we return. 
If index is less than k, then we recur for right part. This reduces the expected complexity from O(n log n) to O(n), with a worst case of O(n^2).


======
partition function 
quick sort function

Three possible cases:
pivot == k 
pivot > k 
k > pivot 
'''


def kth_largest(nums,k):
    k = len(nums)-k # for larges part 
    # purpose of doing this is -> [1,2,8,9]-> when 4-1(k)=3 so kth largest will be in 3 th index 
    def helper(nums,left,right):
        #base case 
        if left > right:
            return 
        pivot_index = partition1(nums,left,right)
        if pivot_index == k:
            return nums[pivot_index]
        elif pivot_index < k: 
            return helper(nums,pivot_index+1,right)
        elif pivot_index > k:
            return helper(nums,left,pivot_index-1)
    return helper(nums,0,len(nums)-1)

def partition1(nums, left,right):
    # middle element 
    pivot = nums[left+(right-left)//2]
    print('pivot is',pivot)
    while left <= right:
        print('nums is',nums)
        while nums[left] < pivot:
            left += 1
        while nums[right] > pivot:
            right -= 1
        if left <= right:
            nums[left],nums[right]=nums[right],nums[left]
            left += 1
            right -= 1
    return left-1 # pivot value  
nums = [3,2,1,5,6,4]
print('kth largest ',kth_largest(nums,2))
nums =[5,2,4,1,3,6,0]
print('kth largest ',kth_largest(nums,4))


print("===another approach ====")

from random import randint

def quick_select(nums: list[int], k: int) -> int:
  k = k-1
  def quick_select_helper(nums: list[int], start: int, end: int,k: int) -> int:
    if start > end: return -1

    pivot = randint(start, end)
    p = partition(nums, start, end, pivot)

    if p == k: 
        return nums[p]
    elif p > k: 
        return quick_select_helper(nums, start, p - 1, k)
    else: 
        return quick_select_helper(nums, p + 1, end, k)

  return quick_select_helper(nums, 0, len(nums) - 1, k)

def partition(nums: list[int], start: int, end: int, pivot: int) -> int:
  nums[pivot], nums[start] = nums[start], nums[pivot]
  left, right = start + 1, end
  while left < right:
    while left < len(nums) and nums[left] < nums[start]:
      left += 1
    while right >= 0 and nums[right] > nums[start]:
      right -= 1
    if left <= right: break
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
  nums[right], nums[start] = nums[start], nums[right]
  return right

nums1 = [3,2,1,5,6,4,0]
print(quick_select(nums1,6)) # return 2
