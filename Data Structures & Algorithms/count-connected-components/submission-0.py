class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]

        for one, two in edges:
            graph[one].append(two)
            graph[two].append(one)
        
        visited = set()
        count = 0 
        def visit(target, parent):
            if target in visited:
                return
            visited.add(target)
            for adj in graph[target]:
                if adj == parent:
                    continue
                visit(adj,target)
            return 
        
        for i in range(n):
            if i not in visited:
                count += 1
                visit(i, -1)
        
        return count 

            
