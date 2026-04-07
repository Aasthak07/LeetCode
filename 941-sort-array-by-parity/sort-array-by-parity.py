class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        #using Binary (inplace)
        start= 0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[start], nums[i] = nums[i], nums[start]
                start+=1
        return nums        

        