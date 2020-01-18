class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        connections = [[1,0], [0,1], [0,-1], [-1,0]]
        stack = [[sr,sc]]
        pixles = set()
        while stack:
            temp = stack.pop()
            pixles.add(tuple(temp))
            for i in connections:
                r = temp[0] + i[0]
                c = temp[1] + i[1]
                if 0 <= r < len(image) and 0 <= c < len(image[0]):
                    if image[r][c] == image[temp[0]][temp[1]] and (r,c) not in pixles:
                        stack.append([r,c])
        
        neighbours = list(pixles)
        for pixel in neighbours:
            r, c = pixel
            image[r][c] = newColor
        
        return image
