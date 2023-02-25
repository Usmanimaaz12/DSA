class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        or_color=image[sr][sc]
        if or_color==color:
            return image
        que=deque()
        que.appendleft((sr,sc))
        m,n=len(image),len(image[0])
      
        directions={(1,0),(-1,0),(0,1),(0,-1)}
        
        image[sr][sc]=color
        while que:
            old_i,old_j=que.pop()
            for di,dj in directions:
                new_i,new_j=old_i+di,old_j+dj
                if (new_i>-1 and new_i<m) and (new_j>-1 and new_j<n) and image[new_i][new_j]==or_color:
                    image[new_i][new_j]=color
                    que.appendleft((new_i,new_j))
        return image
        