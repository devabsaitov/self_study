# from string import ascii_lowercase

# board = [[".", ".", ".", ".", ".", ".", ".", "."],
#          [".", ".", ".", "p", ".", ".", ".", "."],
#          [".", ".", ".", "R", ".", ".", ".", "p"],
#          [".", ".", ".", ".", ".", ".", ".", "."],
#          [".", ".", ".", ".", ".", ".", ".", "."],
#          [".", ".", ".", "p", ".", ".", ".", "."],
#          [".", ".", ".", ".", ".", ".", ".", "."],
#          [".", ".", ".", ".", ".", ".", ".", "."]]

# map_ = dict()
# res , row , col = 0 , [] , []
# for i in range(8):
#     if ["."] * 8 != board[i]:
#         for j in range(8):
#             if board[i][j] == 'R':
#                 find = (i, j)
#                 row = board[i]
#                 col = list(zip(*board))[j]

mat = [
    [1,1,0,0,0],
    [1,1,1,1,1],
    [1,0,0,0,0],
    [1,1,0,0,0],
    [1,1,1,1,1],
]

print(sorted(range(len(mat)) , key =lambda x : sum(mat[x]))[:3])




