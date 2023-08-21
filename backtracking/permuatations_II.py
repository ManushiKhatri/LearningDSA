'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order. 
Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 
'''

def permutations_with_duplicate(nums):
    #edge case 
    if not nums:
        return [[]]
    final_output = []
    #backtrack 
    def helper(pairs,curr_index,visited):
        #base case 
        if len(pairs)==len(nums):
            if pairs not in final_output:
                final_output.append(pairs[:])
                return 
        nums_visited=set()
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                pairs.append(nums[i])
                helper(pairs,i+1,visited)
                visited.remove(i)
                pairs.pop()
    helper([],0,set())
    return final_output 
nums = [1,1,2]
print(permutations_with_duplicate(nums))

# another approach using counter 
from collections import Counter
def permutations(nums):
    #edge case 
    if not nums:
        return [[]]
    final_output = []
    #backtrack 
    def helper(pairs,curr_index,visited,counter):
        #base case 
        if len(pairs)==len(nums):
            if pairs not in final_output:
                final_output.append(pairs[:])
                return 
        nums_visited=set()
        for i in range(len(nums)):
            if counter[nums[i]]>0:
                if i not in visited:
                    visited.add(i)
                    pairs.append(nums[i])
                    counter[nums[i]]-=1
                    helper(pairs,i+1,visited,counter)
                    visited.remove(i)
                    counter[nums[i]]+=1
                    pairs.pop()
    helper([],0,set(),Counter(nums))
    return final_output 
nums = [1,2,2]
print(permutations(nums))

            
'''

Time complexity : O(n!)
T(n) = n * T(n-1) + O(1)

Space Complexity = O(n)
'''
