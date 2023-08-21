'''
Sublist sum to target
You are given a list of non-negative integers. Determine if there is a sub-list (not necessarily consecutive) that sum to a given value.

Examples
sublist_sum([6, 37, 2, 4, 18, 7], 15) -> True
Explanation: Because sum of [6, 2, 7] = 15

sublist_sum([6, 37, 2, 4, 18, 7], 21) -> False
Explanation: No sublist sums to 21

sublist_sum([5, 3, 2, 3], 11) -> True
Explanation: Because sum of [5, 3, 3] = 11

'''

def sublist_sums(nums,target):
   #edge case 
   if len(nums)==0:
       return False 
   if sum(nums)==target:
       return True 
   def backtrack(curr_index,curr_sum):
       #base case 
       if curr_sum==0:
           return True 
       if curr_sum < 0:
           return False
       if len(nums) <= curr_index:
           return False 
       include = backtrack(curr_index+1,curr_sum-nums[curr_index])
       exclude = backtrack(curr_index+1,curr_sum)
       return include or exclude 
   return backtrack(0,target)

nums = [6, 37, 2, 4, 18, 7]
print(sublist_sums(nums,16))#false 
nums = [6, 37, 2, 4, 18, 7]
print(sublist_sums(nums,15))#true 
nums = [6, 3]
print(sublist_sums(nums,9))#true 

'''

f1: sublist_sums
nums	[6, 37, 2, 4, 18, 7]
 
target	15
backtrack	
 
backtrack [parent=f1]
curr_index	0
curr_sum	15
backtrack [parent=f1]
curr_index	1
curr_sum	9
include	False
backtrack [parent=f1]
curr_index	2
curr_sum	9
backtrack [parent=f1]
curr_index	3
curr_sum	7
include	False
backtrack [parent=f1]
curr_index	4
curr_sum	7
include	False
backtrack [parent=f1]
curr_index	5
curr_sum	7
include	True
exclude	False


'''