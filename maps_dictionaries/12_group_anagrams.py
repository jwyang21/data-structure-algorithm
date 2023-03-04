# https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1124/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashdict = {}
        for x in strs:
            hashkey = ''.join(sorted(x))
            if hashkey not in list(hashdict.keys()):
                hashdict[hashkey] = []
            hashdict[hashkey].append(x)
        return [hashdict[x] for x in list(hashdict.keys())]
