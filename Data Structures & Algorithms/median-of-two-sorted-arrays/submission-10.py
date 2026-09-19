class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B, half = nums1, nums2, (len(nums1) + len(nums2)) // 2 
        if len(nums1) > len(nums2): B, A = nums1, nums2 # use smaller array for binary search
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # 1 -> 2 elements
            j = half - (i + 1) - 1 # 2 -> 3 elements
            Aleft, Aright = A[i] if i >= 0 else float('-inf'), A[i + 1] if i + 1 < len(A) else float('inf')
            Bleft, Bright = B[j] if j >= 0 else float('-inf'), B[j + 1] if j + 1 < len(B) else float('inf')
            if Aleft <= Bright and Bleft <= Aright: # correct partition
                if (len(nums1) + len(nums2)) % 2: return min(Aright, Bright)
                else: return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright: r = i - 1
            else: l = i + 1

