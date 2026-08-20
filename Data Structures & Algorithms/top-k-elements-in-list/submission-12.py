class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count, buckets, res = {}, [[] for _ in range(len(nums) + 1)], []
        for num in nums: count[num] = count.get(num, 0) + 1
        for num, freq in count.items():
            buckets[freq].append(num)
        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            for num in bucket:
                res.append(num)
                if len(res) == k: return res
        return res
