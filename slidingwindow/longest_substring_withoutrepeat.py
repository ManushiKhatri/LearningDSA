'''
Given a string s, find the length of the longest substring without repeating characters.

 
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


Approach : 
left pointer right pointer 
shrink the window until no repeating character exist
'''
from collections import defaultdict
def longest_substring_non_repeating(s):
    # variables 
    start,max_length=0,0
    freq=defaultdict(int)
    for end in range(len(s)):
        right_char=s[end]
        freq[right_char]+=1
        #shrink the window 
        while freq[right_char] > 1:
            left_char=s[start]
            freq[left_char]-=1
            if freq[left_char]==0:
                del freq[left_char]
            start+=1
        max_length=max(max_length,end-start+1)
    return max_length
print(longest_substring_non_repeating("abcabcbb"))  #3 
print(longest_substring_non_repeating("pwwkew")) # 3
print(longest_substring_non_repeating("aaaaaaa"))#1

#time complexity -O(n)
#space complexity -> O(len(dict))