# Time Complexity : O(m*n)
# Space Complexity : O(m*n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
#Approach 1: BFS
from typing import List, deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if mat is None or len(mat) == 0:
            return mat
        m= len(mat)
        n = len(mat[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append([i, j])
                else:
                    mat[i][j] = -1
        dist = 1
        while q:
            size = len(q)
            for i in range(0, size):
                curr = q.popleft()
                for dir in dirs:
                    nr = dir[0] + curr[0]
                    nc = dir[1] + curr[1]
                    if(nr >= 0 and nc >= 0 and nr < m and nc < n and mat[nr][nc] == -1):
                        q.append([nr, nc])
                        mat[nr][nc] = dist
            dist+=1
        
        return mat

#Approach 2:DFS
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if mat is None or len(mat) == 0:
            return mat
        m= len(mat)
        n = len(mat[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    mat[i][j] = -1
        dp = [[0] * n for _ in range(m)]
        
        def dfs(mat, i, j):
            #base
            if(i<m-1 and mat[i+1][j]==0): return 1
            if(i > 0 and mat[i-1][j]==0): return 1
            if(j<n-1 and mat[i][j+1]==0): return 1
            if(j > 0 and mat[i][j-1]==0): return 1

            top, bottom = 9999, 9999
            right, left = 9999, 9999

            #top
            if(i > 0 and dp[i-1][j] != 0):
                top = dp[i-1][j]
            
            #left
            if(j > 0 and dp[i][j-1] != 0):
                left = dp[i][j-1]
            
            #bottom
            if(i < m-1):
                if(dp[i+1][j] == 0):
                    dp[i+1][j] = dfs(mat, i+1, j)
                bottom = dp[i+1][j]
            
            #right
            if(j < n-1):
                if(dp[i][j+1] == 0):
                    dp[i][j+1] = dfs(mat, i, j+1)
                right = dp[i][j+1]
            
            return min(right, min(top, min(left, bottom))) + 1

        for i in range(0, m):
            for j in range(0, n):
                if mat[i][j] == -1:
                    dp[i][j]=dfs(mat, i, j)
        return dp
            
            
        
        