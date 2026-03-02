class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26 

        if len(s) != len(t):
            return False

        for i in s:
            ch = ord(i) - ord('a')
            count[ch] += 1
        
        for j in t:
            ch = ord(j) - ord('a')
            count[ch] -= 1

        return all(c == 0 for c in count)
        
        
        
        
        