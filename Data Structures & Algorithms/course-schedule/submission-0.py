class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {i:[] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            hashmap[course].append(prerequisite)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False #cycle detected
            
            if hashmap[course] == []:
                return True #end
            
            #backtrack step to check 
            visited.add(course)
            for prereq in hashmap[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            hashmap[course] = []
            return True
        

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True