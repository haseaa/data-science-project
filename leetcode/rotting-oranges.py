class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total = 0
        row = len(grid)
        visited = set()
        queue = collections.deque()
        minute = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append([i,j])
                    minute.append(0)

        while queue:
            i, j = queue.popleft()
            column = len(grid[i])
            visited.add((i,j))
            time = minute.popleft()
            total = time
            if i-1 >= 0  and grid[i-1][j] == 1 and (i-1,j) not in visited:
                grid[i-1][j] = 2
                queue.append([i-1,j])
                minute.append(time+1)
            if i+1 < row and grid[i+1][j] == 1 and (i+1,j) not in visited:
                grid[i+1][j] = 2
                queue.append([i+1,j])
                minute.append(time+1)
            if j-1 >= 0 and grid[i][j-1] == 1 and (i,j-1) not in visited:
                grid[i][j-1] = 2
                queue.append([i,j-1])
                minute.append(time+1)
            if j+1 < column and grid[i][j+1] == 1 and (i,j+1) not in visited:
                grid[i][j+1] = 2
                queue.append([i,j+1])
                minute.append(time+1)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    total = -1
                    break
        return total