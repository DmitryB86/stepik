mat = [[0,1,2],
       [1,5,3],
       [2,3,4]]
for i in mat:
    for j in i:
        print(j,sep='\n')
    # for j in i:
    #     if mat[i][j]==mat[j][i]:
    #         print(mat[i][j])