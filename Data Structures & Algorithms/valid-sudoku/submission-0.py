class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            nums=[x for x in row if x!="."]
            if len(nums)!=len(set(nums)):
                return False
        for col in range(9):
            nums=[board[row][col] for row in range(9) if board[row][col]!="."]
            if len(nums)!=len(set(nums)):
                return False
        for row_box in range(0,9,3):
            for col_box in range(0,9,3):
                nums=[]
                for row in range(row_box,row_box+3):
                    for col in range(col_box,col_box+3):
                        if board[row][col]!=".":
                            nums.append(board[row][col])
                if len(nums)!=len(set(nums)):
                    return False
        return True





        