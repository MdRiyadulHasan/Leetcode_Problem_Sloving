def kWeakestRows(mat, k):
    sums=[]
    for i, row in enumerate(mat):
        sums.append((sum(row),i))
    sorted_sums=sorted(sums)
    k_rows=sorted_sums[:k]
    res=[]
    for val in k_rows:
        res.append(val[1])
    return res
if __name__ == '__main__':
    mat=[[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
    k=3
    ans =kWeakestRows(mat,k)
    print(ans)
   
