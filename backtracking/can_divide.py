'''
Given an integer array nums, determine if it is possible to divide nums into two groups 
so that the sums of the two groups are equal. 
Explicit constraints: all the multiples of 5 must be in one group, and all the multiples of 3 (that are not a multiple of 5) must be in the other. 
Feel free to write a recursive helper method.

Examples:

nums = [4, 4] → True  
nums = [5, 2] → False  
nums = [5, 2, 3] → True  
nums = [2, 2, 2] → False  
nums = [2, 4, 2] → True  
nums = [5, 5] → False  
nums = [3, 3] → False  
nums = [5, 3, 8] → False
nums = [] → True
nums = [0] → True


'''
def can_divide(nums):
    #edge case 
    if not nums:
        return True 
    def helper(right_sum,left_sum,curr_index):
        #base case 
        # print('right side is',right_sum)
        # print("left side is",left_sum)
        if curr_index == len(nums):
            if right_sum == left_sum:
                return True
            else:
                return False 
        if nums[curr_index] % 5==0:
            left_sum += nums[curr_index]
        elif nums[curr_index] % 3==0:
            right_sum += nums[curr_index]
        else:
            left_group = helper(right_sum,left_sum+nums[curr_index],curr_index+1)
            right_group = helper(right_sum+nums[curr_index],left_sum,curr_index+1)
            return left_group or right_group
        return helper(right_sum,left_sum,curr_index+1)
    return helper(0,0,0)

            
nums = [4, 4]
print(can_divide(nums))
nums = [5,3,8]
print(can_divide(nums))