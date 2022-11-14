# google | microsoft | uber
def spiralOrder( matrix):
    res = []
    left = 0
    right = len(matrix[0])
    top = 0
    bottom = len(matrix)
    while left< right and top<bottom:
        # top row
        for i in range(left, right):
            res.append(matrix[top][i])
        top+=1
        # right column
        for i in range(top,bottom):
            res.append(matrix[i][right-1])
        right-=1
        if not(left<right and top<bottom):
            break;
        # bottom row
        for i in range (right-1, left-1,-1):
            res.append(matrix[bottom-1][i])
        bottom-=1
        # left column
        for i in range(bottom-1,top-1,-1):
            res.append(matrix[i][left])
        left+=1

    return res
