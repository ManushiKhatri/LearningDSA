
'''
you ar given an array of itegeers your taski is to count the numbers of distinc pair same number of digits but differ by one 

[1,151,241,1,9,22,351]

'''
def solution(nums):
    count=0
    set_nums, set_pair = set(nums), set()
    for num in nums:
        str_num_list=list(str(num))
        for i,a in enumerate(str_num_list):
            for b in range(0, 10):
                if str(b) != a:
                    str_num_list[i]=str(b)
                    ns="".join(str_num_list)
                    if ns[0] == "0":
                        continue
                    if(int(ns) in set_nums):
                        set_pair.add(tuple(sorted([int(a), int(ns)])))
    return len(set_pair)
nums = [1,151,241,1,9,22,351]
print(solution(nums))


def solution1(nums):
    from collections import defaultdict

    # HashMap for counting occurrences
    masked_dict = defaultdict(int)
    result = 0

    for num in nums:
        str_num = str(num)
        length = len(str_num)

        # Add the whole number to counteract overcounting
        masked_dict[str_num] += 1
        result -= (masked_dict[str_num] - 1) * length

        # Iterate through the number, masking one digit at a time
        for i in range(length):
            masked_num = str_num[:i] + "X" + str_num[i+1:]
            if masked_num in masked_dict:
                result += masked_dict[masked_num]
            masked_dict[masked_num] += 1

    return result

nums = [1, 151, 241, 1, 9, 22, 351]
print(solution1(nums))  # Expected output: 3
nums1 = [5,5,5,5,5,5,8]
print(solution1(nums1))  # Expected output: 3
nums =[1,11,21,31,41,51,61,71,81,91]
print(solution1(nums))

 # Expected output: 3 (Pairs are (1, 9), (151, 141), and (241, 251))


##
'''
given an array of integers numbers construct a new array un the following manner
first element to first 
2nd element  - last element of the old arrayv 
3rd ele - 2nd element of the old array 
4th element  - second last element of the array  
and so on
example : 
[0,4,3,2,1]
[0,1,4,2,3]

'''
