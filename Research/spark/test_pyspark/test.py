# m : row / n : col / 블록 문자는 A~Z
# return -> 지워지는 블록의 갯수
def solution(m, n, board):
    answer = 0

    num_of_block_deleted = 0
    for i in range(m):
        board[i] = list(board[i])
    for line in board:
        print(line)
    # find

    while True:
        num_of_block_deleted = 0
        delete_loc = []
        for row in range(m - 1):
            for col in range(n - 1):
                if board[row][col] == board[row + 1][col] and board[row][col] == board[row][col + 1] and board[row][
                    col] == board[row + 1][col + 1]:
                    delete_loc.extend([(row, col), (row + 1, col), (row, col + 1), (row + 1, col + 1)])
        delete_set = set(delete_loc)
        num_of_block_deleted = len(delete_set)
        print("delete_set is : ", delete_set)
        print("num_of_block_deleted", num_of_block_deleted)

        # delete
        if num_of_block_deleted == 0:
            break
        else:
            answer += num_of_block_deleted
            for row, col in delete_set:
                board[row][col] = 'x'
        # 재배치

        for col in range(n):
            temp_list = [board[i][col] for i in range(m)]
            temp_list_2 = []
            while 'x' in temp_list:
                temp_list.remove('x')
                temp_list_2.append('x')
            temp_list = temp_list_2 + temp_list
            for i in range(m):
                board[i][col] = temp_list[i]
        for line in board:
            print(line)

    return answer
solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])