def beauty(matrix):
    # Find the beauty of a 2x2 matrix
    values = set(matrix[0] + matrix[1])
    i = 1
    while i in values:
        i += 1
    return i

def solution(numbers):
    # Number of submatrices
    n = len(numbers[0]) // 2
    
    # Compute beauty for each submatrix and store with its index
    beauties = [(beauty([numbers[0][i*2:i*2+2], numbers[1][i*2:i*2+2]]), i) for i in range(n)]
    
    # Sort by beauty
    beauties.sort(key=lambda x: x[0])
    
    # Construct the new matrix using sorted indices
    new_matrix = [[], []]
    for _, idx in beauties:
        new_matrix[0].extend(numbers[0][idx*2:idx*2+2])
        new_matrix[1].extend(numbers[1][idx*2:idx*2+2])

    return new_matrix

# Testing the example
numbers = [[1, 2, 2, 3, 2, 10, 1, 2], [3, 4, 10, 2, 5, 4, 4, 1]]
print(solution(numbers))
# Expected output: [[2, 2, 10, 2, 2, 1, 1, 2], [10, 2, 5, 4, 4, 1, 3, 4]]