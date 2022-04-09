# https://leetcode.com/problems/course-schedule/

from collections import defaultdict

class Solution:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
     
    def DFS_Trasverse(self, v, required):

        required.add(v)
        #print(v, end=' ')
        res = True

        if self.graph[v] != []:
            if not self.graph[v][0] in required:
                res = self.DFS_Trasverse(self.graph[v][0], required)                   
            else:   
                return False 
            
        return res

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        for coursePreq in prerequisites:
            self.addEdge(coursePreq[0], coursePreq[1])

        for coursePreq in prerequisites:
            for prequisite in self.graph[coursePreq[0]]:
                required = set()
                required.add(coursePreq[0])
                isPossible = self.DFS_Trasverse(prequisite, required)
                #print('\n')
                if not isPossible:
                    return False

        return True   

    def test(self, numCourses: int, prerequisites: list[list[int]]):

        for CoursePreq in prerequisites:
            self.addEdge(CoursePreq[0], CoursePreq[1])

        print(self.graph[4])




    def canFinish_failed(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        courseList = {}
        for preReq in prerequisites:
            courseList[preReq[0]] = preReq[1]

        for course in courseList:
            preReqCourse = courseList[course]
            if preReqCourse in courseList and courseList[preReqCourse] == course:
                return False
        
        return True




def main():
    #input = [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]
    #input = [[2,0],[1,0],[3,1],[3,2],[1,3]]
    #input = [[1,0],[0,2],[2,1]]
    #input = [[1,0]]
    input =[[1,4],[2,4],[3,1],[3,2]]
    sol = Solution()
    #sol.test(2,input)  
    print(sol.canFinish(4,input))
    


if __name__ == "__main__":
    main()