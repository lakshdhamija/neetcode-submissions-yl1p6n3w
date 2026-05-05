class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums: freq[num] = freq.get(num, 0) + 1
        print(freq)
        bucket = [[] for _ in range(len(nums) + 1)] # key = freq, val = array of nums with that freq
        for num, f in freq.items():
            bucket[f].append(num)
        res = []
        for freqArr in range(len(bucket) - 1, -1, -1):
            for ele in bucket[freqArr]:
                res.append(ele)
                if len(res) == k: return res
        return res
