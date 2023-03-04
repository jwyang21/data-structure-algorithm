# https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1105/

import numpy as np
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        int_ = np.intersect1d(nums1, nums2)
        return int_.tolist()
