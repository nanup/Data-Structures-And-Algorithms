"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        clonedRoot = Node(node.val)
        
        dic = {node: clonedRoot}
        queue = collections.deque([node])
        
        while queue:
          node = queue.popleft()
          
          for neighbor in node.neighbors:
            if neighbor not in dic:
              clonedNeighbor = Node(neighbor.val)
              dic[neighbor] = clonedNeighbor
              dic[node].neighbors.append(clonedNeighbor)
              queue.append(neighbor)
            else:
              dic[node].neighbors.append(dic[neighbor])
              
        return clonedRoot