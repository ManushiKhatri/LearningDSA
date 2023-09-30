'''
QUICK SORT ALGORITHM 

When n == 1, return immediately
Partition: Divide the problem into 2 
sub problems by selecting a pivot element x and reorganize the array so the left portion has elements <= x and the right portion has elements > x

p           q    r
 <=x   |    x | >x

Once partition is done, 
a recursive call to sort A[p...q-1] and A[q+1...r] will complete the sort.
O(n log n) average, O(n2) worst case


****************
Quick Sort General

Quicksort is a method for sorting an array by repeatedly partitioning it into sub-arrays by:

Selecting an element from the current array. This element is called the pivot element, and in our implementation we used the mid element.
Comparing every element in the array to the pivot element, swap the elements into sides greater than and less than. The partition point in the array is where we guarantee everything before is less and everything after is greater than.
Repeating this process on the sub-arrays separated by the partition point. Do this until a sub-array contains a single element. When the partitioning and swapping are done, the arrays are sorted from smallest to largest.
The worst case runtime for quicksort is O(N^2) and the average runtime for quicksort is O(N logN). The worst case runtime is so unusual that the quicksort algorithm is typically referred to as O(N logN)“



Two works :
• Parition Function 
• Quick Sort Function 

'''



print("quick sort using middle element as pivot element ")
def partition(arr,left,right):
#    print(left,right,'left','right')
   pivot=arr[left+(right-left)//2]# 0 + (8-0)//2 -> 4
#    print('pivot is',pivot)
   while left <= right: # out og bound
      while arr[left] < pivot :
         left += 1
      while arr[right] > pivot :
         right -= 1
      if left <= right:
        arr[left],arr[right]=arr[right],arr[left]
        left +=1
        right -= 1
   return left 

def quick_sort(nums):
  def helper(nums,left,right):
      print('nums is',nums)
      if left > right:
         return 
      pivot_index=partition(nums,left,right)
      if left < pivot_index-1:
         helper(nums,left,pivot_index-1)
      if pivot_index < right:
         helper(nums,pivot_index,right)
  helper(nums,0,len(nums)-1)
  return nums
   
   
nums=[1,9,0,0,2,2,2]
print(quick_sort(nums))


print()
print("=========")
print("ANother approach using pivot as random element")
from random import randint
def quick_sort1(nums: list[int]) -> list[int]:
  def quick_sort_helper(nums: list[int], start: int, end: int) -> None:
    if start >= end: return
    pivot = randint(start, end)
    p = partition1(nums, start, end, pivot)
    quick_sort_helper(nums, start, p - 1)
    quick_sort_helper(nums, p + 1, end)

  quick_sort_helper(nums, 0, len(nums) - 1)
  return nums


def partition1(nums: list[int], start: int, end: int, pivot: int) -> int:
  nums[pivot], nums[start] = nums[start], nums[pivot]
  left, right = start + 1, end
  while left < right:
    while left < len(nums) and nums[left] < nums[start]:
      left += 1
    while right >= 0 and nums[right] > nums[start]:
      right -= 1
    if left >= right: break
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
  nums[right], nums[start] = nums[start], nums[right]
  return right
print(quick_sort1([2,3,7,10,9]))

print()
print("=========")
print("another approach using last element as pivot element ")
def partition2(customList, low, high):
    i = low-1 
    pivot = customList[high]
    for j in range(low,high):
        if customList[j] <= pivot:
            i += 1
            customList[i], customList[j] = customList[j], customList[i]
    customList[i+1], customList[high] = customList[high], customList[i+1]
    return i+1

def quick_sort2(nums):
  def quickSort(nums, low, high):
      if low < high:
          pi = partition2(nums, low, high)
          quickSort(nums, low, pi-1)
          quickSort(nums, pi+1, high)
  quickSort(nums,0,len(nums)-1)
  return nums
print(quick_sort2([0,1,1,0,2,2]))
#best case nlogn 
# worst case O(n2)-one half is null and naother half is calling recursiely



