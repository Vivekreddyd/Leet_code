class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for row in range(len(board)):
            for column in range(len(board[0])):
                # if(column==word[0]):
                if self.dfs(row, column, word, board):
                    return True
        return False

    def dfs(self, i, j, wrd, brd):
        if len(wrd) == 0:
            return True
        if i < 0 or i >= len(brd) or j < 0 or j >= len(brd[0]) or not wrd[0] == brd[i][j]:
            return False
        # tmp = brd[i][j]
        brd[i][j] = '#'
        res = self.dfs(i + 1, j, wrd[1:], brd) or self.dfs(i - 1, j, wrd[1:], brd) or self.dfs(i, j + 1,wrd[1:],brd) or self.dfs(i, j - 1, wrd[1:], brd)
        # brd[i][j] = tmp
        return res
        # m=len(board)
        # n=len(board[0])
        # visited=[]
        # for i,row in enumerate(board):
        #     for j,column in enumerate(row):
        #         if column==word[0]:
        #             temp_i,temp_j=i,j
        #             visited.append(tuple((i,j)))
        #             flag=True
        #             for w in range(1,len(word)):
        #                 if temp_j+1<=n-1 and word[w]==board[temp_i][temp_j+1] and (temp_i,temp_j+1) not in visited:
        #                     visited.append(tuple((temp_i,temp_j+1)))
        #                     temp_j+=1
        #                     continue
        #                 elif temp_j-1>=0 and word[w]==board[temp_i][temp_j-1] and (temp_i,temp_j-1) not in visited:
        #                     visited.append(tuple((temp_i,temp_j-1)))
        #                     temp_j-=1
        #                     continue
        #                 elif temp_i+1<=m-1 and word[w]==board[temp_i+1][temp_j] and (temp_i+1,temp_j) not in visited:
        #                     visited.append(tuple((temp_i+1,temp_j)))
        #                     temp_i+=1
        #                     continue
        #                 elif temp_i-1>=0 and word[w]==board[temp_i-1][temp_j] and (temp_i-1,temp_j) not in visited:
        #                     visited.append(tuple((temp_i-1,temp_j)))
        #                     temp_i-=1
        #                     continue
        #                 else:
        #                     visited=[]
        #                     flag=False
        #                     break
        #             if flag==True:
        #                 return True
        # return False
ip_array=[["C","A","A"],["A","A","A"],["B","C","D"]]
temp=Solution()
print(temp.exist(ip_array,"AAB"))