class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = -101
        slow = 0
        fast = 1
        while fast < len(nums) and slow < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
            else:
                fast += 1
        for i in range(slow+1, len(nums)):
            nums[i] = -101
        return slow + 1
        