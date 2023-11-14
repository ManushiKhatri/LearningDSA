'''
#leetcode 153 
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 


'''
# since it needs to be done within logn time 
# lets do in binary search 
def minimum_element(nums):
    left , right = 0 , len(nums)-1
    while left < right:
        print('right left is ', right, left)
        mid = (left+right) // 2
        
        if nums[mid] <= nums[right]:
            right = mid 
        else:
            left = mid + 1
    return nums[left]
nums = [11, 13,15,17]
print(minimum_element(nums)) # 11 
nums = [4, 5, 6, 7, 0, 1]
print(minimum_element(nums)) # 0

'''
(1) loop is left < right, which means inside the loop, left always < right
(2 ) since we use round up for mid, and left < right from (1), right would never be the same as mid
(3) Therefore, we compare mid with right, since they will never be the same from (2)
(4) if nums[mid] < nums[right], we will know the minimum should be in the left part, so we are moving right.
We can always make right = mid while we don't have to worry the loop will not ends. Since from (2), we know right would never be the same as mid, making right = mid will assure the interval is shrinking.
(5) if nums[mid] > nums[right], minimum should be in the right part, so we are moving left. Since nums[mid] > nums[right],mid can't be the minimum, we can safely move left to mid + 1, which also assure the interval is shrinking

'''