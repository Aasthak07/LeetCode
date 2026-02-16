class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        # Copy nums2 elements into nums1
        for i in range(n):
            nums1[m + i] = nums2[i]
        
        # Sort nums1
        nums1.sort()
