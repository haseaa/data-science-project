class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        setNums1 = set(nums1)
        setNums2 = set(nums2)
        output = []
        distinct1 = []
        for nums in nums1:
            if nums not in setNums2:
                distinct1.append(nums)
        output.append(list(set(distinct1)))
        distinct2 = []
        for nums in nums2:
            if nums not in setNums1:
                distinct2.append(nums)
        output.append(list(set(distinct2)))
        return output
