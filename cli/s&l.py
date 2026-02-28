import random
import time

# Board configuration: key -> destination when landed on key
SNAKES = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
LADDERS = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

def roll_dice():
    return random.randint(1, 6)

def move_player(pos, roll):
    new = pos + roll
    if new > 100:
        return pos  # must land exactly on 100
    # snakes and ladders
    if new in SNAKES:
        return SNAKES[new]
    if new in LADDERS:
        return LADDERS[new]
    return new

def play_game(num_players=2, seed=None, delay=0.5):
    if seed is not None:
        random.seed(seed)
    positions = [0] * num_players
    turn = 0
    while True:
        player = turn % num_players
        roll = roll_dice()
        old = positions[player]
        new = move_player(old, roll)
        positions[player] = new
        print(f"Player {player+1} rolled {roll}: {old} -> {new}", end="")
        # indicate snake or ladder
        if new != old + roll and new != old:
            if new > old + roll:
                print("  climbed a ladder!")
            else:
                print("  bitten by a snake!")
        else:
            print()
        if new == 100:
            print(f"Player {player+1} wins!")
            return player+1
        turn += 1
        time.sleep(delay)

if __name__ == "__main__":
    print("Starting Snakes and Ladders (2 players).")
    winner = play_game(num_players=2, seed=None, delay=0.2)