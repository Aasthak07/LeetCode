class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        product= 1
        sum_of_digits= 0

        while temp>0:
            r= temp%10
            temp//=10
            sum_of_digits+=r
            product*=r

        return product - sum_of_digits    




    
        