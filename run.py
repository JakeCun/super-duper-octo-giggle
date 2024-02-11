# Define the size of the grid
grid_size = 5

# Create an empty grid
player_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
computer_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

# Display the grids (for testing purposes)
print("Player's Grid:")
for row in player_grid:
    print(" ".join(row))

print("\nComputer's Grid:")
for row in computer_grid:
    print(" ".join(row))

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

def place_ship(grid, ship_number):
    """
    Function to place a ship of size one on the grid.
    Args:
        grid (list): The grid where the ship will be placed.
        ship_number (int): The number of the ship being placed.
    """
    print(f"Place Ship {ship_number}:")
    while True:
        try:
            # Get input from the player for ship placement
            row = int(input(f"Enter the row (0-{grid_size - 1}): "))
            col = int(input(f"Enter the column (0-{grid_size - 1}): "))
            
            # Check if the input coordinates are within the grid boundaries
            if 0 <= row < grid_size and 0 <= col < grid_size:
                # Check if the chosen cell is empty and not already occupied by another ship
                if grid[row][col] == '.':
                    # Place the ship
                    grid[row][col] = 'X'
                    break
                else:
                    print("Error: That cell is already occupied. Please choose another location.")
            else:
                print(f"Error: Coordinates must be within the range 0-{grid_size - 1}. Please try again.")
        except ValueError:
            print("Error: Please enter a valid integer.")

def display_grids():
    """
    Function to display both player's and computer's grids.
    """
    print("Player's Grid:")
    for i in range(grid_size):
        for j in range(grid_size):
            print(revealed_player_grid[i][j], end=' ')
        print()
    
    print("\nComputer's Grid:")
    for i in range(grid_size):
        for j in range(grid_size):
            print(revealed_computer_grid[i][j], end=' ')
        print()

# Function to generate random ships for the computer player
def generate_ships(grid):
    for _ in range(4):  # Generate 4 ships
        while True:
            row = random.randint(0, grid_size - 1)
            col = random.randint(0, grid_size - 1)
            if grid[row][col] == '.':
                grid[row][col] = 'X'
                break

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
                computer_score += 1
            else:
                print("Computer missed!")
                revealed_player_grid[row][col] = 'O'
            break

def check_win():
    """
    Function to check if either player has won the game.
    Returns:
        str: 'player' if the player wins, 'computer' if the computer wins, or None if the game is ongoing.
    """
    # Check if all of the player's ships are sunk
    if all(cell == 'O' for row in computer_grid for cell in row):
        return 'player'
    # Check if all of the computer's ships are sunk
    elif all(cell == 'O' for row in player_grid for cell in row):
        return 'computer'
    else:
        return None

# Place ships for the player
print("Player, please place your ships:")
for ship_number in range(1, 5):  # Player places 4 ships
    place_ship(player_grid, ship_number)

# Generate ships for the computer player
generate_ships(computer_grid)

# Display both grids at the beginning of the game
display_grids()

# Game loop
while True:
    # Player's turn
    player_turn()
    display_grids()
    print(f"Player's Score: {player_score}")
    print(f"Computer's Score: {computer_score}")
    if check_win() == 'player':
        print("Congratulations! You")
