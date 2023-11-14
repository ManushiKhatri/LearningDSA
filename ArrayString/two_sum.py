'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


'''


def twoSum(nums, target):
    # Create a dictionary to store the difference between the target and each element
    pairs = {}

    # Iterate through the list of numbers
    for i in range(len(nums)):
        # Calculate the difference between the target and the current element
        diff = target - nums[i]
        print("pairs is",pairs)

        # Check if the current element is already in the dictionary
        if nums[i] in pairs:
            # If it is, return the indices of the two elements that add up to the target
            return [pairs[nums[i]], i]
        else:
            # If the current element is not in the dictionary, store the difference and its index
            pairs[diff] = i
print(twoSum([2, 7,11,15],9))