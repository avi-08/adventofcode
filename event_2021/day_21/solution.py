import os


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_path, 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    return [int(x.split()[-1]) for x in lines]


def get_die_rolls(a):
    an = a % 100
    an1 = (a + 1) % 100
    return a % 100, an + 1,  an1 + 1

def get_next(pos, jump, scale=10):
    mod = (pos + jump) % scale
    return scale if mod == 0 else mod

def deterministic_play(p1, p2):
    score1, score2, z = [0] * 3
    turn = 0
    while score1 < 1000 and score2 < 1000:
        turn += 1
        x, y, z = get_die_rolls(z+1)
        if turn % 2 == 0:
            p2 = get_next(p2, x + y + z)
            score2 += p2
        else:
            p1 = get_next(p1, x + y + z)
            score1 += p1
    print(f"Final positions: p1[{p1}], p2[{p2}]")
    return score1, score2, turn


def quantum_play(p1, p2, score1, score2, turn):
    if score1 >= 21:
        return 1, 0
    elif score2 >= 21:
        return 0, 1
    
    p1_wins, p2_wins = 0, 0
    if turn % 2 == 0:
        for i in range(1, 4):
            p2 = get_next(p2, i, 3)
            score2 += p2
            x, y = quantum_play(p1, p2, score1, score2, turn + 1)
            p1_wins += x
            p2_wins += y
    else:
        for i in range(1, 4):
            p1 = get_next(p1, i, 3)
            score1 += p1
            x, y = quantum_play(p1, p2, score1, score2, turn + 1)
            p1_wins += x
            p2_wins += y
    return p1_wins, p2_wins
    

def main():
    p1, p2 = read_input('sample.txt')
    print(f"Starting positions of p1: {p1} and p2: {p2}")
    
    # Part one
    score1, score2, turn = deterministic_play(p1, p2)
    winner = "p1" if score1 > score2 else "p2"
    print(f"Winner is player {winner}. Score: {max(score1, score2)}")
    print(f"Die rolled: {turn * 3} times. Scores: p1[{score1}], p2[{score2}]. Answer: [{turn * 3 * min(score1, score2)}]")
    
    # Part two
    p1_wins, p2_wins = quantum_play(p1, p2, 0, 0, 1)
    goat = "p1" if p1_wins > p2_wins else "p2"
    print(f"Player 1 won in {p1_wins} universes. Player2 won in {p2_wins} universes")
    print(f"And the greatest of all time player is: {goat}")


if __name__ == '__main__':
    main()