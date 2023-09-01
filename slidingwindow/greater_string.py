'''

Given a word , rearrange the letters of  to construct another word  in such a way that  is lexicographically greater than . In case of multiple possible answers, find the lexicographically smallest one among them.

Input Format

The first line of input contains , the number of test cases. Each of the next  lines contains .

Constraints

 will contain only lower-case English letters and its length will not exceed .
Output Format

For each testcase, output a string lexicographically bigger than  in a separate line. In case of multiple possible answers, print the lexicographically smallest one, and if no answer exists, print no answer.

Sample Input

ab = [ab,ba]return ba 
baca=[aacb,...,baca,bcaa,...]=return bcaa 


'''
def next_highest_word(string):
    S = [ord(i) for i in string]
    print('s is',S)
    #find non-incresing suffix from last
    i = len(S) - 1
    while i > 0 and S[i-1] >= S[i]:
        i = i - 1
    if i <= 0:
        return 'no answer'

    #next element to highest is pivot
    j = len(S) - 1
    while S[j] <= S[i -1]:
        j = j - 1
    S[i-1],S[j] = S[j],S[i-1]

    #reverse the suffix
    S[i:] = S[len(S) - 1 : i-1 : -1]
    ans = [chr(i) for i in S]
    ans = "".join(ans)
    return ans 
print(next_highest_word('bazb')) #bcaa