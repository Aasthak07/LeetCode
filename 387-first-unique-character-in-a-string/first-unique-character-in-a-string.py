class Solution:
    def firstUniqChar(self, s: str) -> int:
        # n= len(s)
        # st= set({})
        # ans=0
        # for i in range(n-1, -1, -1):
        #     if s[i] not in st:
        #         ans=i
        #         st.add(s[i])
        # return ans    
        freq={}
        for i in s:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        for i in range(len(s)):
            if freq[s[i]] ==1:
                return i
        return -1                   