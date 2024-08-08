class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        stack = [0]
        while stack:
            vis = stack.pop()
            visited.add(vis)
            for room in rooms[vis]:
                if vis in visited:
                    if room not in visited:
                        stack.append(room)
                    visited.add(room)
        if len(visited) == len(rooms):
            return True
        else:
            return False