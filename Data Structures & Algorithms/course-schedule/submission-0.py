class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(visit, value):
            nonlocal course
            visit.add(value)
            for temp in course[value]:
                if temp in visit or not dfs(visit, temp):
                    return False 
            visit.remove(value)
            return True

        course = [[] for i in range(numCourses)]
        for pre in prerequisites:
            course[pre[0]].append(pre[1])
        print(course)

        for i in range(numCourses):
            if not dfs(set(), i):
                return False
        
        return True 