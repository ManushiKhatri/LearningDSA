'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
from trie import Trie

# longest_common_prefix.py
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    trie = Trie()
    if not strs:
        return ""
        
    for word in strs:
        trie.insert_string(word)

    current = trie.root
    longest = ''
    first_word = strs[0]

    for char in first_word:
        print('current children is',current.children)
        if len(current.children) > 1 or current.end_of_string:
            return longest
            
        longest += char
        current = current.children[char]
            
    return longest

        
strs = ["flower","flow","floww"] 
print(longestCommonPrefix(strs)) # flow
strs = ['ab','a'] 
print(longestCommonPrefix(strs)) # a