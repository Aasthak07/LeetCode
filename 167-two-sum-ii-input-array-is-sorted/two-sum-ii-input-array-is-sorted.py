class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n= len(nums)
        # dict1={}
        # for i in range(n):
        #     rem= target- nums[i]
        #     if rem in dict1:
        #         return [dict1[rem]+1,i+1]
        #     dict1[nums[i]]=i 

        left=0
        right= len(nums)-1
        while left<right:
            sum1=nums[left] + nums[right]
            if sum1== target:
                return [left+1, right+1]
            elif sum1>target:
                right-=1
            else:
                left+=1          
        