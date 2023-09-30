
'''

The procedure MAX-HEAPIFY on the facing page maintains the max-heap prop- erty.
Its inputs are an array A with the heap-size attribute and an index i into the array. When it is called, 
MAX-HEAPIFY assumes that the binary trees rooted at LEFT .i/ and RIGHT .i/ are max-heaps, but that AŒi� might be smaller than its chil- dren, thus violating the max-heap property. MAX-HEAPIFY lets the value at AŒi� <üoat down= in the max-heap so that the subtree rooted at index i obeys the max- heap property. 

'''
#following the procedure of max heapify // 
#min heapify can be done in similar way 

def heapify(A, i, heapSize): #O(lgn)
    l = left(i)
    r = right(i)
    
    largest = i
    
    if l < heapSize and A[l] > A[i]:
        largest = l
        
    if r < heapSize and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, largest, heapSize)

def left(i):
    return 2 * i

def right(i):
    return (2 * i) + 1

def parent(i):
    return i // 2

def buildHeap(A, heapSize): #o(n)
    for i in range(len(A)//2,-1,-1):
        heapify(A, i, heapSize)

#heap sort algorithm -O(nlogn)
def heapSort(A):
  heapSize = len(A)
  buildHeap(A, heapSize)
  for i in range(len(A)-1,0,-1): #O(n)
    A[0], A[i] = A[i], A[0]
    heapSize -= 1
    heapify(A, 0, heapSize) #O(lgn)
  return A
b=[5,3,17,10,84,19,6,22,9]
print(heapSort(b))

'''
The HEAPSORT procedure takes O.n lg n/ time, since the call to BUILD-MAX- HEAP takes O.n/ time and each of the n  1 calls to MAX-HEAPIFY takes O. lg n/ time. 

'''


        
    