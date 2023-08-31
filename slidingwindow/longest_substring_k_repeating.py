'''
Given a string s and an integer k, 
return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

if no such substring exists, return 0.


Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.


'''
from collections import defaultdict
def longest_substring(s,k):
    #initiate tracking variables 
    freq = [0]*26 # storing the frequency of every characters 
    for i in range(len(s)):
        freq[ord(s[i])-ord('a')] += 1
    unique = 0 #unique elements 
    for i in range(len(freq)):
        if freq[i]!= 0:
            unique += 1
    # idea is to break the sliding window whose freq is less than k 
    start,max_length = 0,0
    for end in range(len(s)):
        count = freq[ord(s[end])-ord('a')]
        if count < k:
            max_length=max(max_length,end-start)
            start = end + 1
    return max_length
print(longest_substring("aaabb",3))
print(longest_substring("aaabcccc",3)) #4 
            
        