'''
Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

Examples

Image of Subtree Sum example
Input: root = [5,2,-3]
Output: [2,-3,4]

#idea 
traverse through each root and add the value of left and right and root 
store that in frequency to identiy max freq of sum 
'''
"""
Algorithms : 

Setup: create a dictionary that maps node values to nodes to ids
1) Create a hashmap to store frequencies of sums
2) Traverse the tree
3) When we visit a node, generate its subtree sum
    - This will equal the value of its left subtree sum + value of its right subtree sum + the node's value
    - The left/right subtree sums can be computed recursively as we visit
4) Once we generate the subtree's sum s, increment frequency of s by 1 in the hashmap (or set frequency to 1 if this is first time adding that key to map)
5) Return the computed subtree sum so that the caller (the node's parent) can use it to calculate its own subtree sum
6) After traversal is complete, iterate over the hashmap, tracking the highest frequency sum and the frequency at which it appears
    - Keep a list that contains the sums with highest frequency so far, and a variable tracking the highest frequency encountered
    - If we encounter a key (a subtree sum) whose value (the frequency of that sum) exceeds the highest frequency encountered, we reset the list to only contain that key, and update the variable tracking highest frequency encountered
    - If we encounter a key (a subtree sum) whose value (the frequency of that sum) equals the highest frequency encountered, then add that key to the list
    - At the end of this iteration, we will have the list of subtree sums with highest frequency


"""
from tree_node import root_from_list,pretty_print
def most_frequent_subtree(root):
    if not root:
        return []
    freq={}
    def dfs(node):
        #base case 
        if not node:
            return 0
        subtree_sum = dfs(node.left)+dfs(node.right)+node.val 
        if subtree_sum not in freq:
            freq[subtree_sum]=1
        else:
            freq[subtree_sum]+=1
        return subtree_sum
    dfs(root)
    final_output =[]
    highest_freq=0
    for key in freq:
        if len(final_output)==0:
            final_output.append(key)
            highest_freq=freq[key]
        elif freq[key]==highest_freq:
            final_output.append(key)
        elif freq[key] > highest_freq:
            highest_freq=freq[key]
            final_output=[key]
    print('freq is',freq)
    return final_output 
root = root_from_list([5,2,-3])

print(most_frequent_subtree(root))#[2,-3,4]

root1 = root_from_list([5,2,5])
pretty_print(root1)
print(most_frequent_subtree(root1)) # [2]

root2 = root_from_list([3])
print(most_frequent_subtree(root2)) # [3]