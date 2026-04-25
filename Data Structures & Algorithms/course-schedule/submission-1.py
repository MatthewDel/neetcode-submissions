class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(visit, value):
            nonlocal course, cleared
            if value in cleared:
                return True 
            visit.add(value)
            for temp in course[value]:
                if temp in visit or not dfs(visit, temp):
                    return False 
            visit.remove(value)
            cleared.add(value)
            return True

        cleared = set()
        course = [[] for i in range(numCourses)]
        for pre in prerequisites:
            course[pre[0]].append(pre[1])
        print(course)

        for i in range(numCourses):
            if not dfs(set(), i):
                return False
        
        return True 