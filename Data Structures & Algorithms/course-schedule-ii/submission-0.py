class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        checked = set()
        visited = set()
        sol = []

        courses = [[] for i in range(numCourses)]

        for course, pre in prerequisites:
            courses[course].append(pre)
        
        def dfs(target):
            if target in visited:
                return False 
            if target in checked:
                return True 
            visited.add(target)
            for pre in range(len(courses[target])):
                if not dfs(courses[target][pre]):
                    return False 
            visited.remove(target)
            sol.append(target)
            checked.add(target)
            return True

        for course in range(len(courses)):
            if not dfs(course):
                return []

        return sol 
            