class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeroCounter = 0
        pointer = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCounter += 1
            else:
                nums[pointer] = nums[i]
                pointer += 1
        for i in range(pointer, len(nums)):
            nums[i] = 0