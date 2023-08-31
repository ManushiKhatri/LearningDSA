'''
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.
Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:
Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
p=1
q=1 



'''
from collections import Counter
def check_anagram(s,p):
    pattern_freq=Counter(p)
    start,matched = 0,0
    final_output = []
    for end in range(len(s)):
        right_char = s[end]
        #check in the pattern freq
        if right_char in pattern_freq:
            pattern_freq[right_char]-=1
            if pattern_freq[right_char]==0:
                matched += 1
                
        if matched == len(pattern_freq):
            final_output.append(start) #starting indices 
            
        #shrink the window
        if end >= len(p)-1:#index start with 0 so 
            left_char = s[start]
            start += 1
            if left_char in pattern_freq:
                if pattern_freq[left_char]==0:
                    matched -= 1
                pattern_freq[left_char]+=1
    return final_output

String="abbcabc"
Pattern="abc"
print(check_anagram(String,Pattern)) # [2,3,4]
print(check_anagram("ppqp","pq"))#[1,2]
            
        
        
        