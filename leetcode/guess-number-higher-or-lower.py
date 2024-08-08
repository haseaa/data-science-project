# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        while True:
            tebak = (l + n)//2
            g = guess(tebak)
            if g == 0:
                return tebak
            elif g == 1:
                l = tebak + 1
            else:
                n = tebak