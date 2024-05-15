# Time Complexity : O(m*n)
# Space Complexity : O(m*n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
#Approach 1: BFS
from typing import List, deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image is None or len(image)==0:
            return image

        m = len(image)
        n = len(image[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        if(image[sr][sc] == color):
            return image
        
        orgColor = image[sr][sc]

        q = deque()
        q.append(sr)
        q.append(sc)
        image[sr][sc] = color

        while q:
            cr = q.popleft()
            cc = q.popleft()

            for dir in dirs:
                nr = cr + dir[0]
                nc = cc + dir[1]

                if(nr >= 0 and nc >= 0 and nr < m and nc < n and image[nr][nc] == orgColor):
                    q.append(nr)
                    q.append(nc)
                    image[nr][nc] = color
        
        return image
    
#Approach 2: DFS
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image is None or len(image)==0:
            return image

        m = len(image)
        n = len(image[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        if(image[sr][sc] == color):
            return image
        
        orgColor = image[sr][sc]

        def dfs(sr, sc, image):
            #base
            if(sr < 0 or sc < 0 or sr == m or sc == n or image[sr][sc] != orgColor):
                return

            #logic
            image[sr][sc] = color
            for dir in dirs:
                nr = dir[0] + sr
                nc = dir[1] + sc
                dfs(nr, nc, image) 

        dfs(sr, sc, image)
        return image
    

                
        