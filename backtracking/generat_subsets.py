'''
Given an integer list nums (no duplicates), return all possible subsets of nums (any order) (as lists, not sets). 
Your output must not contain duplicate subsets. Feel free to write a recursive helper method.

Example:

nums = [1,2,3] → 
       [
        [1,2,3],
        [1,2],
        [2,3],
        [1,3],
        [1],
        [2],
        [3],
        []
      ]

'''
def generate_subsets(nums):
    #edge case 
    if not nums:
        return [[]]
    #initiate variable 
    final_output =[]
    def helper(curr_index,pairs):
        #base case 
        if curr_index >= len(nums):
            final_output.append(pairs[:])
            return 
        pairs.append(nums[curr_index])
        #Include 
        helper(curr_index+1,pairs)
        #exclude 
        pairs.pop()
        helper(curr_index+1,pairs)
    helper(0,[])
    return final_output 
nums = [1,2,3]
print(generate_subsets(nums))
nums = [1,1]
print(generate_subsets(nums))
