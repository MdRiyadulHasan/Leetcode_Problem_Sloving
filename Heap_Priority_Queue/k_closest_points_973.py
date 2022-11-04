import heapq
def kClosest( points, k):
    minheap =[]
    for x,y in points:
        dist=(x**2)+(y**2)
        minheap.append([dist,x,y])
    heapq.heapify(minheap)
    res=[]
    while k>0:
        dist,x,y=heapq.heappop(minheap)
        res.append([x,y])
        k-=1
    return res
    
if __name__ == '__main__':
    points=[[3,3],[5,-1],[-2,4]]
    k=2
    ans =kClosest(points,k)
    print(ans)