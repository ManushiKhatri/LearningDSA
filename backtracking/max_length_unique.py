'''
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.


Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.


'''
def longest_unique_characters(arr):
    # Edge case
    if not arr:
        return 0
    max_length = [0]
    def helper(curr_index, pairs):
        # Base case 
        if curr_index >= len(arr):
            curr_string = ''.join(pairs[:])
            if len(curr_string) == len(set(curr_string)):
                max_length[0] = max(max_length[0], len(curr_string))
            return 
        # Include 
        pairs.append(arr[curr_index])
        helper(curr_index+1, pairs)
        
        # Exclude 
        pairs.pop()
        helper(curr_index+1, pairs)
    helper(0, [])
    return max_length[0]
arr = ["un","iq","ue"]
print(longest_unique_characters(arr))  # Expected output: 4
arr = ["abcdefghijklmnopqrstuvwxyz"]
print(longest_unique_characters(arr))  # Expected output: 26

