class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        rs = ''
        par = []
        number = ''
        for i in s:
            if i.isnumeric():
                number += i
            elif i == '[':
                stack.append(int(number))
                par.append('')
                number = ''
            elif i == ']':
                app = par.pop()
                app *= stack.pop()
                if len(stack) == 0:
                    rs += app
                else:
                    par[-1] += app
            else:
                if len(par) == 0:
                    rs += i
                else:
                    par[-1] += i
        return rs