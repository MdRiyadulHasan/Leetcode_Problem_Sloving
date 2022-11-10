# math
# google
def validSquare( p1, p2, p3, p4):
    def dist(A,B):
        return (A[0]-B[0])**2 + (A[1]-B[1])**2
    
    distance=[dist(p1,p2), dist(p1,p3), dist(p1,p4),dist(p2,p3),dist(p2,p4),dist(p3,p4)]
    distance.sort()
    return 0 <distance[0]==distance[1]==distance[2]==distance[3] and 2*distance[0]==distance[-1]==distance[-2]
if __name__ == '__main__':
    p1 = [1,0],
    p2 = [-1,0],
    p3 = [0,1],
    p4 = [0,-1]
    ans = validSquare(p1,p2,p3,p4)
    print(ans)