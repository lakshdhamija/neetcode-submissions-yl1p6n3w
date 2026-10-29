class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets, countsMap = [[] for _ in range(len(nums) + 1)], {}
        for num in nums: countsMap[num] = countsMap.get(num, 0) + 1
        for num, freq in countsMap.items(): buckets[freq].append(num)
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            bucketArr = buckets[i]
            for num in bucketArr:
                if len(res) < k: res.append(num)
            if len(res) == k: break
        return res
        