class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        prefix_xor = 0
        freq = {0: 1}
        ans = 0

        for num in nums:
            prefix_xor ^= num
            ans += freq.get(prefix_xor, 0)
            freq[prefix_xor] = freq.get(prefix_xor, 0) + 1

        return ans