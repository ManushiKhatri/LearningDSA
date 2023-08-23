'''
Merge Sort Algorithm 

• When n == 1, return immediately
• Split array in half and recursively sort each half
• Merge the sorted halves into a final sorted sequence
• O(n log n) average, O(n log n) worst case


'''
#first part 
def merge_sort(lst):
  if len(lst) <= 1:
    return lst
  middle = len(lst) // 2
  left = lst[:middle]
  right = lst[middle:]
  sleft = merge_sort(left)
  print('sleft is ',sleft)
  sright = merge_sort(right)
  print('sright is',sright)
  return merge(sleft, sright)

#seconde part 
def merge(left, right):
  result = []
  while (left and right):
    print('final result is',result)
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)
  if left:
    result += left
  if right:
    result += right
  return result

lst = [1,2,4,5,6,6,7,321,2,23,412,4,21,1]
print(merge_sort(lst))



print("another approach")
def merge_sort2(lst): # nlogn 
    if len(lst) <=1:
        return lst 
    mid = len(lst)//2
    left = merge_sort2(lst[:mid])
    right = merge_sort2(lst[mid:])
    return mergee(left,right)
    
   
#merge two sorted arrays
def mergee(lst1,lst2): # o(n)
    i,j=0,0
    result = []
    while i < len(lst1) or j < len(lst2):
        if i >= len(lst1):
            result += lst2[j:]
            break 
        elif j >= len(lst2):
            result += lst1[i:]
            break 
        elif lst1[i] < lst2[j]:
            result.append(lst1[i])
            i+=1
        else:
            result.append(lst2[j])
            j+=1
    return result 
lst1=[2, 3, 4, 1, 5, 3, 67, 8]
print(merge_sort2(lst1))
    
    