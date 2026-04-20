class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))  # remove duplicates
        
        if len(unique_nums) < 3:
            return max(unique_nums)  # if less than 3 distinct numbers
        
        unique_nums.sort(reverse=True)  # sort descending
        return unique_nums[2]  # third maximum