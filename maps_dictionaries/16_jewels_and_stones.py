# https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1136/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        all_jewels = list(jewels)
        cnt = 0
        for x in list(stones):
            if x in all_jewels:
                cnt += 1 
        return cnt
        
