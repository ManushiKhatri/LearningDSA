'''
Given an integer array nums, and an integer target, write a function that determines how many expressions are possible which evaluate to target adding binary operators +, -, and * between the digits in nums. Feel free to write a recursive helper method.

Note: You can ignore order of operations for this problem, just go left to right.

Examples:

nums = [1, 2, 3], target = 6 → 2 (expressions: 1 + 2 + 3, 1 * 2 * 3) 
nums = [1, 2, 5], target = 7 → 1 (expression: 1 * 2 + 5) 
nums = [0, 0], target = 0 → 3 (expressions: 0 - 0, 0 + 0, 0 * 0)


'''
def count_expressions(nums,target):
    #base case 
    def helper(index,curr_value):
        #base case 
        if len(nums)==index:
            if curr_value==target:
                return 1 
            return 0
        #recursive calls
        addition = helper(index+1,curr_value+nums[index])
        subtract = helper(index+1,curr_value-nums[index])
        mutiply = helper(index+1,curr_value*nums[index])
        return addition+subtract+mutiply
    return helper(1,nums[0])
nums = [1,2,5]
print(count_expressions(nums,0))      