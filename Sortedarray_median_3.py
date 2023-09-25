def findMedianSortedArrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    mid = len(merged) // 2
    if len(merged) % 2 == 0:
        return (merged[mid - 1] + merged[mid]) / 2.0
    else:
        return float(merged[mid])
nums1 = [1, 3]
nums2 = [2]
result1 = findMedianSortedArrays(nums1, nums2)
print(result1) 