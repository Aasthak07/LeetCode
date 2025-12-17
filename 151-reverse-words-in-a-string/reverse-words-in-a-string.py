class Solution:
    def reverseWords(self, s: str) -> str:
        # s=s.strip()
        # s=s.split()
        # s.reverse()
        # return " ".join(s)
        s=s.strip()
        s=s.split()
        i=0
        j=len(s)-1

        while i<j:
            # s[i], s[j] = s[j], s[i]  # swap
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
            i+=1
            j-=1

        return " ".join(s)    

        

    
        