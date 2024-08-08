class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        """
        323 -> 323 - 320 = 3
        32 -> 32 - 30 = 2
        3 -> 3 - 0 = 3
        21 -> 21 - 20 = 1
        2 -> 2 - 0 = 2
        211 -> 211 - 210 = 1
        6556 -> 6556 - 6550 = 6
        556 -> 655-650 = 5
        65 -> 65-60 = 5
        6 -> 6-0 = 6
        """
        pangkat = 0
        y = []
        penyimpan = x
        if x < 0:
            return False
        else:
            while x > 0:
                pangkat += 1
                modulo = x % 10
                y.append(modulo)
                x //= 10
            for angka in y:
                pangkat -= 1
                x += angka * 10**pangkat
            if x == penyimpan:
                return True
            else:
                return False