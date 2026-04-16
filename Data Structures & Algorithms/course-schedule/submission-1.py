class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap= {i:[] for i in range(numCourses)}
        for courses, pre in prerequisites:
            premap[courses].append(pre)
        
        visitset = set()

        def dfs(crs):
            if crs in visitset:
                return False #because cycle is detected
            if premap[crs] == []:
                return True #no prereqs
            #visited course add to visitset
            visitset.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            visitset.remove(crs)
            premap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

        #o(v+e) - t,s
