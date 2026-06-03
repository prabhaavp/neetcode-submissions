class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        m = []
        for index, element in enumerate(nums):
            if element in d: 
                d[element] += 1
            else: 
                d[element] = 1
        res = []
        for num, count in d.items():
            heapq.heappush_max(m, (count, num)) 
        print(m)

        for i in range(k):
            res.append(heapq.heappop_max(m)[1])
            print(m)
        return res

'''
[1,2,2,3,3,3]

1
1

2
1 (1), 2 (1)

2
1 (1), 2 (2)

3
1 (1), 2 (2). 3 (1)

                heapq.heappush_max(m, (d[element],element)) 

'''