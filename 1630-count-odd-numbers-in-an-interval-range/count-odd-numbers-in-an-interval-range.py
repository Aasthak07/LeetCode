# class Solution:
#     def countOdds(self, low: int, high: int) -> int:
#         count = 0
#         for i in range(low, high + 1):
#             if i % 2 != 0:    # agar odd hai
#                 count += 1
#         return count
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return ((high - low) // 2) + (1 if low % 2 != 0 or high % 2 != 0 else 0)
