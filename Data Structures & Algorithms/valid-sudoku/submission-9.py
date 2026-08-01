class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isvalid = True
        centers = []
        sub_sections = dict()
        sub_sections_list = list()
        col_list = []
        row_list = []
        # board=[[".",".","5",".",".",".",".",".","6"],
        #         [".",".",".",".","1","4",".",".","."],
        #         [".",".",".",".",".",".",".",".","."],
        #         [".",".",".",".",".","9","2",".","."],
        #         ["5",".",".",".",".","2",".",".","."],
        #         [".",".",".",".",".",".",".","3","."],
        #         [".",".",".","5","4",".",".",".","."],
        #         ["3",".",".",".",".",".","4","2","."],
        #         [".",".",".","2","7",".","6",".","."]]


        def is_integer(s):
            try:
                int(s)
                return True
            except ValueError:
                return False

        for i in range(1, len(board), 3):
            for j in range(1, len(board[0]), 3):
                centers.append((i, j))

        for center in centers:
            added = 0
            row, col = center
            sub_sections[center] = set()
            sub_sections_list = []

            for i in [-1, 0, +1]:
                for j in [-1, 0, +1]:
                    if is_integer(board[row+i][col+j]):
                        if center in sub_sections:
                            sub_sections[center].add(board[row + i][col + j])
                        else:
                            sub_sections[center] = {board[row + i][col + j]}
                        
                        sub_sections_list.append(board[row + i][col + j])



            if len(sub_sections_list) != len(sub_sections[center]):
                # print(sub_sections_list)
                # print(sub_sections[center])
                isvalid = False

        # for i in range(len(board[0])):
        #     for j in range(len(board)):
        #         inverted_board[i][j] = board[j][i]
        # print(inverted_board)

        for row in range(len(board[0])):
            row_list = [board[row][x] for x in range(9) if is_integer(board[row][x])]
            row_set = set(row_list)
            if len(row_list) != len(row_set):
                print(row, row_list, row_set)
                isvalid = False
        
        for col in range(len(board[0])):
            col_list = [board[x][col] for x in range(9) if is_integer(board[x][col])]
            col_set = set(col_list)
            if len(col_list) != len(col_set):
                print(col, col_list, col_set)
                isvalid = False


        return isvalid