import heapq
def lastStoneWeight(stones):
    stones=[-s for s in stones]
    heapq.heapify(stones)
    while len(stones)>1:
        first = heapq.heappop(stones)
        second=heapq.heappop(stones)
        if second>first:
            heapq.heappush(stones, second-first)
    stones.append(0)
    return abs(stones[0])
if __name__ == '__main__':
    stones=[2,7,4,1,8,1]
    ans =lastStoneWeight(stones)
    print(ans)