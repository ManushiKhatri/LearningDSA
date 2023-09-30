'''
The output should be in the same length of the input or the word 
since I was guarateed to have the same length for both and 
there're 3 possible outcomes for each character. 
"G" green if the character is in the word and at the same index,
"Y" yellow if the character is in the word but not in the same index, 
"R" red if the character is not in word at all.

Ex. word: "game", input_word: "stma"OUTPUT: "RRGY"


'''
#brute force approch 
def guess_word(word,input_word):
    #guaranted to  have same length then we can only iterate to one
    unique = set(word)  #len(n)
    output = ''
    for i in range(len(input_word)): # O(n)
        if input_word[i] in unique:
            if input_word[i]==word[i]:
                output += 'G'
            else:
                output += 'Y'
        else:
            output += 'R'
    return output
'''
TC= O(N)
SC=O(n)

'''
print(guess_word('game','stma')) # RRGY
print(guess_word('game','eamg')) # YGGY
print(guess_word('mess','goat')) # 'RRRR'
      
    