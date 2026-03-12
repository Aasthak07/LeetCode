# Consider all possible subarrays.
# For each subarray, calculate number of distinct elements.
# Put all those values into a new array called the uniqueness array.
# Sort that array.
# Return the median of that array.
# If two medians exist, take the smaller one
# | Subarray | Distinct Elements |
# | -------- | ----------------- |
# | [1]      | 1                 |
# | [2]      | 1                 |
# | [3]      | 1                 |
# | [1,2]    | 2                 |
# | [2,3]    | 2                 |
# | [1,2,3]  | 3                 |
# Number of subarrays of an array of size n:== 𝑛(𝑛+1)//2




from typing import List
from collections import defaultdict

class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        target = (total + 1) // 2
        
        def count(k):
            freq = defaultdict(int)
            left = 0
            res = 0
            
            for right in range(n):
                freq[nums[right]] += 1
                
                while len(freq) > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1
                
                res += right - left + 1
            
            return res
        
        low, high = 1, len(set(nums))
        
        while low < high:
            mid = (low + high) // 2
            
            if count(mid) >= target:
                high = mid
            else:
                low = mid + 1
        
        return low
        