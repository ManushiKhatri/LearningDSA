### MAX-HEAPIFY Procedure

**Purpose**: Ensure that the subtree rooted at index `i` obeys the max-heap property.

**Inputs**: 
- `A`: An array representing the heap
- `i`: The index of the node where the max-heap property might be violated

```python
MAX_HEAPIFY(A, i):
    l = LEFT(i)
    r = RIGHT(i)
    if l <= len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]  # exchange A[i] with A[largest]
        MAX_HEAPIFY(A, largest)
