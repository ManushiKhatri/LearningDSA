'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Constraints
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
Examples
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Input: nums = [0,1]
Output: [[0,1],[1,0]]

making decision tree:
        1
    2   3
3         2


'''

def permutations(nums):
    #edge case 
    if not nums:
        return [[]]
    final_output = []
    #backtrack 
    def helper(curr_index,pairs,visited):
        # base case 
        if len(pairs)==len(nums):
            final_output.append(pairs[:])
            return 
        #exploring all the choices 
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                pairs.append(nums[i])
                print("pairs is",pairs)
                helper(i+1,pairs,visited)
                visited.remove(i)
                pairs.pop()
    helper(0,[],set())
    return final_output
nums,nums1=[1,2,3],[]
print(permutations(nums))
print(permutations(nums1))
            

