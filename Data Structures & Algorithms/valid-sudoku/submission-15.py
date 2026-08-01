class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isvalid = True
        centers = []
        sub_sections_list = list()
        col_list = []
        row_list = []

        for i in range(1, len(board), 3):
            for j in range(1, len(board[0]), 3):
                centers.append((i, j))

        for center in centers:
            added = 0
            row, col = center
            sub_sections = set()
            sub_sections_list = []

            for i in [-1, 0, +1]:
                for j in [-1, 0, +1]:
                    if board[row+i][col+j] != ".":
                        sub_sections.add(board[row + i][col + j])
                        sub_sections_list.append(board[row + i][col + j])

            if len(sub_sections_list) != len(sub_sections):
                isvalid = False

        for row in range(len(board[0])):
            row_list = [board[row][x] for x in range(9) if (board[row][x]) != "."]
            row_set = set(row_list)
            if len(row_list) != len(row_set):
                print(row, row_list, row_set)
                isvalid = False
        
        for col in range(len(board[0])):
            col_list = [board[x][col] for x in range(9) if board[x][col] != "."]
            col_set = set(col_list)
            if len(col_list) != len(col_set):
                print(col, col_list, col_set)
                isvalid = False


        return isvalid