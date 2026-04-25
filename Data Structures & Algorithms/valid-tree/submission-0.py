class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for i in range(n)]

        for one, two in edges:
            graph[one].append(two)
            graph[two].append(one)
        
        visited = set()
        checked = set()

        def valid(target, parent):
            if target in visited:
                return False
            visited.add(target)
            for adj in graph[target]:
                if adj == parent:
                    continue 
                if not valid(adj, target):
                    return False 
            return True
        
        return valid(0, -1) and len(visited) == n
                
            