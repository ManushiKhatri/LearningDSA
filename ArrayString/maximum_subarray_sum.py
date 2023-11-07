'''
# leetcode 53; https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

'''
# using kadanes algorithm 
# ignore the curr sum if its less than 0 
# max sum will be the one which is greater than curr sum 
def maximum_subarray_sum(arr):
    max_sum = float("-inf") # in the case if every element in the array is negative 
    curr_sum = 0
    for index in range(len(arr)):
        curr_sum += arr[index]
        if curr_sum > max_sum: # store max sum
            max_sum = curr_sum 
        if curr_sum < 0: # when array has sum negative set it to 0 because when we move it to next element negative sum wont be helpful 
            curr_sum = 0 
    return max_sum 
arr = [5,4,-1,7,8]
print(maximum_subarray_sum(arr)) # 23
arr=[-1,-2,-8]
print(maximum_subarray_sum(arr)) # - 1


print("==========subarray====")
# let's modify the problem , what if we need to return the sub array itself instead of max sum only 
def maximumsum_subarray(arr):
    max_sum = float("-inf")
    curr_sum = 0
    max_subarray = []
    curr_subarray = []

    for num in arr:
        curr_sum += num
        curr_subarray.append(num)
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_subarray = curr_subarray
        if curr_sum < 0:
            curr_sum = 0
            curr_subarray = []
    return max_subarray

arr = [5, 4, -1, 7, 8]
print(maximumsum_subarray(arr))  # [5, 4, -1, 7, 8]
arr = [-1, -2, -8]
print(maximumsum_subarray(arr))  # [-1]
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximumsum_subarray(arr))  # [4, -1, 2, 1]
