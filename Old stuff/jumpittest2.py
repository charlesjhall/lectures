
def main():
    #board = [0, 24, 17, 15, 61, 49, 61, 8, 65, 43, 26, 99, 7, 57, 97, 50, 93, 6, 82, 52]
    def jump_it(self: list) -> int:
        board = [0, 24, 17, 15, 61, 49, 61, 8, 65, 43, 26, 99, 7, 57, 97, 50, 93, 6, 82, 52]
        lowest_numbers_list = []
        for x in board:
            while board[x] != board[(len(board)]:
                elif board[:2] >= board[:3]:
                    return lowest_numbers_list + jump_it(board[:3])
                elif board[:2] < board[:3]:
                    return lowest_numbers_list + jump_it(board[:2])
            else:
                return lowest_numbers_list + board[len(board)]

        total = sum(lowest_numbers_list)
        print(total)

    jump_it(board)

if __name__ == '__main__':
    main()