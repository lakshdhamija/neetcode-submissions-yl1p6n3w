class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxBucket, seen = [[] for i in range(len(nums) + 1)], {}
        for num in nums: seen[num] = seen.get(num, 0) + 1
        for key, val in seen.items():
            maxBucket[val].append(key)
        res = []
        for i in range(len(maxBucket) - 1, -1, -1):
            curArr = maxBucket[i]
            for ele in maxBucket[i]:
                res.append(ele)
                if len(res) == k: return res