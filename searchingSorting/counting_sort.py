'''
[7, 12, 3, 5, 3, 12, 19, 16, 20, 18, 20]

Finally, create an empty result list. Iterate through your buckets – for each bucket i with value x, add x i’s to your result list.


[0, 0, 0, 2, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 1, 1, 2]

[3, 3, 5, 7, 12, 12, 16, 18, 19, 20, 20]

You can do this in O(k + n) time where n is the number of elements.


'''

#counting sort algorithm 
def counting_sort(nums,max):
    bucket = [0]*(max+1)
    for num in nums:
        bucket[num]+=1
    result = []
    #iterate through buckets 
    for i in range(len(bucket)):
        i_count = bucket[i]
        print('i count is',i_count)
        for count in range(i_count):
            result += [i]
    return result 
            
print(counting_sort([1,2,9,6,4,5],9))
    