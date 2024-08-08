import collections

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        output = ""
        totalR = 0
        totalD = 0
        queue = collections.deque()
        for rights in senate:
            if rights == 'D' and totalR == 0:
                queue.append('D')
                if queue[0] == 'R':
                    queue.popleft()
                else:
                    totalD += 1
            elif rights == 'R' and totalD == 0:
                queue.append('R')
                if queue[0] == 'D':
                    queue.popleft()
                else:
                    totalR += 1
            elif rights == 'R' and queue[0] != 'R' and totalD > 0:
                totalD -= 1
            elif rights == 'D' and queue[0] != 'D' and totalR > 0:
                totalR -= 1
        
        if len(queue) != 0:
            output = queue[0]
        if output == 'D' or totalD > 0:
            return 'Dire'
        elif output == 'R' or totalR > 0:
            return "Radiant"
