'''
1. Combinations
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Examples
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

'''

def combinations(n,k):
    #edge case 
    if k==0:
        return []
    # initating tracking variables 
    final_output = []
    #helper function to explore all the choices 
    def helper(pairs,curr_num):
        #base case
        if len(pairs)==k:
            final_output.append(pairs[:])
            return 
        # explore choices 
        for i in range(curr_num,n+1):
            #append the current value 
            pairs.append(i)
            #explore all remaining choices 
            helper(pairs,i+1)
            #backtrack 
            pairs.pop()
    helper([],1)
    return final_output 
print(combinations(4,2))

'''
ouptut scenarios: 

curr -> 1 
i-> 1
pairs [1]

curr -> 1
i-> 2
[1,2]

curr-> 3 
pairs==k
return None 

pairs.pop()-> [1]
curr-> 1
i->3
[1,3]

--repeat the process for all possible choices ---


'''