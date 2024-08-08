class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 1
        isSum = False
        slow = 0
        fast = 1
        lastHigh = nums[0]
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                total += 1
                fast += 1
            else:
                total -= 1
                fast += 1
            if total == 0:
                total += 1
                slow = fast
                fast = slow + 1
        return nums[slow]
