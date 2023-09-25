def findMedianSortedArrays(nums1, nums2):
    merged = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])

    total_length = len(merged)
    if total_length % 2 == 0:
        mid1 = total_length // 2
        mid2 = mid1 - 1
        return (merged[mid1] + merged[mid2]) / 2.0
    else:
        mid = total_length // 2
        return merged[mid]

nums1 = [1, 3]
nums2 = [2]
result1 = findMedianSortedArrays(nums1, nums2)
print(result1) 
