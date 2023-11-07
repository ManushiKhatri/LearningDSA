
#qsn : https://www.chegg.com/homework-help/questions-and-answers/given-board-cells-containing-bubble-specific-color-task-emulate-bubble-popping-game-game-p-q118840390?fbclid=IwAR3N5KS6YXAgc-oO4sYRASRviyFqtBEK-b-hDECFq_x-znyeV7IJdFXVEQs

def solution(bubbles, operations):
    # Helper function to get diagonal neighbors
    def diagonal_neighbors(i, j, rows, cols):
        neighbors = []
        if i - 1 >= 0 and j - 1 >= 0:  # Top-left
            neighbors.append((i - 1, j - 1))
        if i - 1 >= 0 and j + 1 < cols:  # Top-right
            neighbors.append((i - 1, j + 1))
        if i + 1 < rows and j - 1 >= 0:  # Bottom-left
            neighbors.append((i + 1, j - 1))
        if i + 1 < rows and j + 1 < cols:  # Bottom-right
            neighbors.append((i + 1, j + 1))
        return neighbors

    # Helper function to drop the bubbles down after popping
    def drop_bubbles(bubbles):
        rows, cols = len(bubbles), len(bubbles[0])
        for j in range(cols):
            # Filter out zeros (empty spaces) and collect the bubbles for the column
            filled = [bubbles[i][j] for i in range(rows) if bubbles[i][j] != 0]
            # Fill with zeros (empty spaces) at the top
            for i in range(rows - len(filled)):
                bubbles[i][j] = 0
            # Place the bubbles at the bottom
            for i in range(len(filled)):
                bubbles[rows - len(filled) + i][j] = filled[i]

    rows, cols = len(bubbles), len(bubbles[0])
    for op in operations:
        i, j = op
        if bubbles[i][j] == 0:
            continue  # Skip if the cell is empty
        color = bubbles[i][j]
        bubbles[i][j] = 0  # Pop the clicked bubble
        for ni, nj in diagonal_neighbors(i, j, rows, cols):
            if bubbles[ni][nj] == color:
                bubbles[ni][nj] = 0
        drop_bubbles(bubbles)  # Drop remaining bubbles to fill empty cells

    return bubbles


# Example usage
bubbles = [
    [2, 1, 2, 6, 2],
    [1, 5, 6, 2, 4],
    [2, 6, 1, 4, 2],
    [6, 7, 3, 1, 4]
]
operations = [[2, 3], [2, 3], [0, 3], [2, 1]]
result = solution(bubbles, operations)
print(result)  # [[0, 0, 0, 0, 0], [2, 1, 2, 0, 0], [1, 5, 1, 6, 0], [2


bubbles = [
    [1, 1, 1,4,3],
    [4, 1, 2,3,3],
    [1, 5, 1,1,2],
    [4, 3, 2,2,4]
]
operations = [[1, 1], [3, 3],[2,2],[3,0]]

result = solution(bubbles, operations)
print('result is',result )