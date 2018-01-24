class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def dup(list_input):
            for x in list_input:
                temp={}
                for y in x:
                    if y in temp and not y==".":
                        return 0
                    temp[y]=1
            return 1
        rows=[[]*t for t in range(len(board))]
        cols=[[]*t for t in range(len(board))]
        boxes=[[]*t for t in range(len(board))]
        for ind,i in enumerate(board):
            rows.append(list(i))
            for indx,j in enumerate(i):
                cols[indx].append(j)
                boxes[(int(ind/3)*3)+int(indx/3)].append(j)
        ret_row=dup(rows)
        ret_col=dup(cols)
        ret_box=dup(boxes)
        if not ret_row or not ret_col or not ret_box:
            return False
        else:
            return True
#         row=list(set(i))
#         row.remove('.')
#         row_val=dup(row)
        # for row in rows:
        #     row_val=
test=Solution()
board=[[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
print(test.isValidSudoku(board))