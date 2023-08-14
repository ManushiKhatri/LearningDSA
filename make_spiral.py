"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]

"""
def make_spiral(n):
 f n <= 0:
        return []
    result = [[None for i in range(n)] for j in range(n)]
    xBeg,xEnd = 0,n-1
    yBeg,yEnd = 0,n-1
    current = 1
    while (True):
        for i in range(yBeg,yEnd+1):
            result[xBeg][i] = current
            current += 1
        xBeg += 1
        if (xBeg > xEnd):
            break
        for i in range(xBeg,xEnd+1):
            result[i][yEnd] = current
            current += 1
        yEnd -= 1
        if (yEnd < yBeg):
            break
        for i in range(yEnd,yBeg-1,-1):
            result[xEnd][i] = current
            current += 1
        xEnd -= 1
        if (xEnd < xBeg):
            break
        for i in range(xEnd,xBeg-1,-1):
            result[i][yBeg] = current
            current += 1
        yBeg += 1
        if (yBeg > yEnd):
            break
    return result