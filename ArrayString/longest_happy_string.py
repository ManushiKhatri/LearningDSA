'''
leetcode 1405 : https://leetcode.com/problems/longest-happy-string/


A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.

'''
# contiguous longest substring 
# track the charcter with high freq - lets use heap for that 
# using heap 
import heapq
def longest_substring(a, b, c):
    pairs = [(a, 'a'), (b, 'b'), (c, 'c')]
    max_heap = []
    final_substring = " "
    # Ignore if any of the char has 0 count
    for count, char in pairs:
        if count > 0:
            max_heap.append((-count, char))

    heapq.heapify(max_heap)

    while max_heap:
        print('max heap is ',max_heap)
        count, char = heapq.heappop(max_heap)
        if len(final_substring) > 1 and final_substring[-1] == final_substring[-2] == char:
            if not max_heap:
                break
            # Pop again
            count1, char1 = heapq.heappop(max_heap)
            final_substring += char1
            count1 += 1
            if count1 != 0:
                heapq.heappush(max_heap, (count1, char1))
        else:
            final_substring += char
            count += 1
        # add until it is possible 
        if count != 0:
            heapq.heappush(max_heap, (count, char))
    return final_substring

print(longest_substring(1, 1, 7)) # ccaccbcc
print(longest_substring(0, 0, 7)) # cc 

    

