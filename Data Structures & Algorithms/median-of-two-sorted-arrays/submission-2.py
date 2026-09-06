class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArr = []
        l1, l2 = 0, 0
        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] < nums2[l2]:
                mergedArr.append(nums1[l1])
                l1 += 1
            else:
                mergedArr.append(nums2[l2])
                l2 += 1
        while l1 < len(nums1):
            mergedArr.append(nums1[l1])
            l1 += 1
        while l2 < len(nums2):
            mergedArr.append(nums2[l2])
            l2 += 1
        # print(mergedArr, len(mergedArr) // 2, (len(mergedArr) // 2) + 1)
        if len(mergedArr) % 2: return mergedArr[len(mergedArr) // 2]
        else:
            return (mergedArr[len(mergedArr) // 2] + mergedArr[(len(mergedArr) // 2) - 1]) / 2