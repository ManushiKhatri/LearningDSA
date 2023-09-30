def solution(numbers):
    # Determine the current player's turn based on the number of pairs removed
    player = 0  # 0 for Alice and 1 for Bob

    while True:
        found_pair = False
        i = 0
        while i < len(numbers) - 1:
            if numbers[i] == numbers[i + 1]:
                # Skip the pair
                i += 2
                found_pair = True
            else:
                i += 1

        # If a pair is not found, the current player loses
        if not found_pair:
            return 'Alice' if player == 1 else 'Bob'

        # Switch to the next player
        player = 1 - player
    

numbers1 = [1, 4, 5, 5, 6]
numbers2 = [1, 3, 3, 1, 5]
numbers3 = [1, 2, 2, 3, 3, 1, 1]

print(solution(numbers1))  # Alice
print(solution(numbers2))  # Bob
print(solution(numbers3))  # Alice



    
    
        
        
    