
def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    tot = [0, cost[0]]
    for i in range(1, len(cost)):
        print(tot)
        index = (i+1)//2
        if i % 2:
            index = (i+1)//2
            ma = min(cost[i], tot[index])
            tot[index] = ma
        else:
            ma = min(tot[index]+cost[i], cost[i-1])
            tot.append(ma)
    return tot[-1]
cost = [1,100,1,1,1]
print(minCostClimbingStairs(cost))