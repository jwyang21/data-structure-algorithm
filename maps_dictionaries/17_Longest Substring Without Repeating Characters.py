#https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1135/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        used_chars = {}
        
        left = 0
        
        for right, char in enumerate(s):
            if char in used_chars and left <= used_chars[char]: #Duplicated character
                left = used_chars[char] + 1
            else:
                ans = max(ans, right - left + 1)
            used_chars[char] = right
            
        return ans
        
