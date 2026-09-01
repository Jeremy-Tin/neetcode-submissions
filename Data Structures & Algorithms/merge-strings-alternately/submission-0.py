class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_len = max(len(word1), len(word2))
        len1, len2 = len(word1), len(word2)
        s = []
        
        for i in range(max_len):
            if i < len1:
                s.append(word1[i])
            if i < len2:
                s.append(word2[i])
        
        return "".join(s)