class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # i=0
        # total_cost=0
        # while(i<len(cost)-1):
        #     if(cost[i]<cost[i+1]):
        #         total_cost+=cost[i]
        #         i+=1
        #     else:
        #         total_cost+=cost[i+1]
        #         i+=2
        # if(i==len(cost)-2):
        #     return total_cost
        # elif(i==len(cost)-3):
        #     return total_cost+min(cost[i],cost[i+1])
        # return total_cost
        n = len(cost)
        if n == 0 or n == 1:
            return 0
        min_cost0, min_cost1 = cost[0], cost[1]
        for i in range(2, n):
            min_cost0, min_cost1 = min_cost1, min(min_cost0, min_cost1) + cost[i]

        return min(min_cost0, min_cost1)
temp=Solution()
cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
temp.minCostClimbingStairs(cost)