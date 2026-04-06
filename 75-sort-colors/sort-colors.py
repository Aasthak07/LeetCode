from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = [0] * 3  # since only 0,1,2

        # count frequencies
        for num in nums:
            freq[num] += 1

        # overwrite nums in-place
        index = 0
        for i in range(3):
            while freq[i] > 0:
                nums[index] = i
                index += 1
                freq[i] -= 1