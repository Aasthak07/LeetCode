from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        maj_length = n // 2
        freq = {}

        for i in nums:
            if i in freq:          # ✅ fixed
                freq[i] += 1
            else:
                freq[i] = 1

        for j in freq:
            if freq[j] > maj_length:
                return j           # ✅ return element