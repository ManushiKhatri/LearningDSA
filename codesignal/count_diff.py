''''
For numbers = [1, 151, 241, 1, 9, 22, 3511 , the output should be solution (numbezs)
3
RULES
• numbers [0] = 1 differs from numbers[41 = 9 on the one and only digit in both numbers.
• numbers[1] = 151 differs from numbers|6] = 351 on the first digit.
• numbers[3] = 1 differs from numbers [4] = 9 on the one and only digit in both numbers.
README
SETTINGS
Note that numbers[0] = 1 and numbers[3] = 1 do not differ from each other at all and
thus do not count as a valid pair.


'''


def solution(nums):
    final_result = 0
    encodings, visited = {},{}
    for num in nums:
        str_num = str(num)
        for i in range(len(str_num)):
            num_encoding = str_num[:i] + "*" + str_num[i + 1:]
            if num_encoding not in encodings:
                encodings[num_encoding] = 0
            else:
                encodings[num_encoding] += 1
                if num in visited:
                    final_result += encodings[num_encoding] - visited[num]
                else:
                    final_result += encodings[num_encoding]
        if num not in visited:
            visited[num] = 0
        visited[num] += 1
    return final_result 
print(solution([1, 151, 241, 1, 9, 22, 351]))