import os


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.curdir, file_name)

    with open(file_path, 'r') as f:
        bingo_input = f.readlines()
    temp = bingo_input[0].strip().split(",")
    print(temp)
    nums = [int(x) for x in temp]

    boards = []
    i = 2
    while i < len(bingo_input):
        board = []
        total = 0
        while i < len(bingo_input) and len(bingo_input[i].strip()) != 0:
            temp = bingo_input[i].strip().split()
            board.append([int(x) for x in temp])
            total += sum(board[-1])
            board[-1].append(0)
            i += 1
        i += 1
        board.append([0] * len(board[0]))
        board[-1][-1] = total
        boards.append(board)

    return nums, boards


def play_to_win(n, boards, winners):
    won = []
    for bi, board in enumerate(boards):
        if bi in winners:
            continue
        for ri, r in enumerate(board[:-1]):
            for ci, _ in enumerate(r[:-1]):
                if board[ri][ci] == n:
                    boards[bi][ri][-1] += 1
                    boards[bi][-1][ci] += 1
                    boards[bi][-1][-1] -= n
                    boards[bi][ri][ci] = -1
                    if 5 in (board[ri][-1], board[-1][ci]):
                        won.append(bi)
    return won


def play(nums, boards, win_at, winners):
    for n in nums:
        print(f"Play with {n}")
        winner = play_to_win(n, boards, winners)
        if len(winner) > 0:
            print(f"Bingo!! Winning number: {n}")
            for w in winner:
                print(f"Board {w + 1} wins")
                winners.append(w)
            if len(winners) >= win_at:
                print(f"Bingo!! To win at position {win_at}, number: {n}")
                print(f"Board {winners[win_at-1] + 1} wins at position {win_at}. Value: {boards[winners[win_at-1]]} ")
                print(f"Score: {boards[winners[win_at-1]][-1][-1] * n}")
                break
    return winners

def main():
    nums, boards = read_input('sample.txt')
    print(f"Total nums: {len(nums)} nums: {nums}")
    print(f"Total boards: {len(boards)}")

    winners = []

    # Part one
    winners = play(nums=nums, boards=boards, win_at=1, winners=winners)

    for i, board in enumerate(boards):
        print(f"Board {i + 1}: {board}")

    print("\n<=============>\n")

    # Part two
    winners = play(nums=nums, boards=boards, win_at=len(boards), winners=winners)
    
    for i, board in enumerate(boards):
        print(f"Board {i + 1}: {board}")


if __name__ == '__main__':
    main()
