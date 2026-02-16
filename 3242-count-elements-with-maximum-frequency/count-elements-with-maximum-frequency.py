class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        from collections import Counter
        
        freq = Counter(nums)           # Count frequency of each number
        max_freq = max(freq.values())  # Find maximum frequency
        
        count = 0
        for value in freq.values():
            if value == max_freq:
                count += value
        
        return count
