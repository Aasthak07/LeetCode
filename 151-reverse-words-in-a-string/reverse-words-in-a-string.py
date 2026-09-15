class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""

        # Extract words manually
        for ch in s:
            if ch != " ":
                word += ch
            else:
                if word != "":
                    words.append(word)
                    word = ""

        # Add last word
        if word != "":
            words.append(word)

        # Build answer in reverse order
        ans = ""
        for i in range(len(words) - 1, -1, -1):
            ans += words[i]
            if i != 0:
                ans += " "

        return ans