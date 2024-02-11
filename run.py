import random

# Define the size of the grid
grid_size = 5

# Create empty grids for the player and computer
player_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
computer_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
revealed_player_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
revealed_computer_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

# Track the score for both the player and the computer
player_score = 0
computer_score = 0

# Function to randomly place ships on the grid
def place_ships_randomly(grid):
    ship_locations = set()
    while len(ship_locations) < 4:  # Place 4 ships
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        ship_locations.add((row, col))
    for row, col in ship_locations:
        grid[row][col] = 'X'

# Function to display both player's and computer's grids with hidden ships
def display_grids_with_hidden_ships():
    print("Player's Grid:")
    for i in range(grid_size):
        for j in range(grid_size):
            if player_grid[i][j] == '*' or (player_grid[i][j] == 'X' and revealed_player_grid[i][j] == 'X'):
                print('*', end=' ')  # If player's ship is hit or revealed, show '*'
            elif player_grid[i][j] == 'X':
                print('@', end=' ')  # Show player's ships as '@'
            else:
                print(revealed_player_grid[i][j], end=' ')
        print()
    
    print("\nComputer's Grid:")
    for i in range(grid_size):
        for j in range(grid_size):
            if revealed_computer_grid[i][j] == 'X':
                print('*', end=' ')  # If computer's ship is hit, show '*'
            else:
                print(revealed_computer_grid[i][j], end=' ')
        print()





def player_turn():
    """
    Function to handle the player's turn.
    """
    global player_score
    print("\nPlayer's Turn:")
    while True:
        try:
            # Get input from the player for attacking the computer's grid
            row = int(input(f"Enter the row to attack (0-{grid_size - 1}): "))
            col = int(input(f"Enter the column to attack (0-{grid_size - 1}): "))
            
            # Check if the input coordinates are within the grid boundaries
            if 0 <= row < grid_size and 0 <= col < grid_size:
                # Check if the chosen cell has not been attacked before
                if revealed_computer_grid[row][col] == '.':
                    # Check if the chosen cell contains a ship
                    if computer_grid[row][col] == 'X':
                        print("Hit!")
                        revealed_computer_grid[row][col] = 'X'
                        player_score += 1
                        if player_score == 4:
                            return 'player'
                    else:
                        print("Miss!")
                        revealed_computer_grid[row][col] = 'O'
                    break
                else:
                    print("Error: You've already attacked this cell. Please choose another location.")
            else:
                print(f"Error: Coordinates must be within the range 0-{grid_size - 1}. Please try again.")
        except ValueError:
            print("Error: Please enter a valid integer.")

def computer_turn():
    """
    Function to handle the computer's turn.
    """
    global computer_score
    print("\nComputer's Turn:")
    while True:
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        
        # Check if the chosen cell has not been attacked before
        if revealed_player_grid[row][col] == '.':
            # Check if the attack hits or misses
            if player_grid[row][col] == 'X':
                print("Computer hit!")
                revealed_player_grid[row][col] = 'X'
                player_grid[row][col] = 'X'  # Update player's grid
                computer_score += 1
                if computer_score == 4:
                    return 'computer'
            else:
                print("Computer missed!")
                revealed_player_grid[row][col] = 'O'
            break

# Place ships randomly for both player and computer
place_ships_randomly(player_grid)
place_ships_randomly(computer_grid)

# Display both grids with hidden ships at the beginning of the game
display_grids_with_hidden_ships()

# Game loop
while True:
    # Player's turn
    result = player_turn()
    computer_turn()
    print("\n\n")
    display_grids_with_hidden_ships()
    print(f"Player's Score: {player_score}")
    print(f"Computer's Score: {computer_score}")
    if result == 'player':
        print("Congratulations! You win!")
        break
    elif result == 'computer':
        print("Computer wins! Better luck next time.")
        break
