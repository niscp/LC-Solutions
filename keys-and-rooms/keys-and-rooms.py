class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        number_of_rooms = len(rooms)
        visited = [False for _ in range(number_of_rooms)]
        visit(0, visited, rooms)
            
        for room in visited:
            if not room:
                return False
        return True
            

def visit(room_number, visited, rooms):
    stack = [room_number]
    while len(stack):
        room_here = stack.pop()
        visited[room_here] = True
        keys = rooms[room_here]
    
        for key in keys:
            if visited[key]:
                continue
            stack.append(key)
        