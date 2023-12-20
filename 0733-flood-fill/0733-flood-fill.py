class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        start_color = image[sr][sc]
        
        def flood_fill(x, y):
            if x < 0 or x >= len(image): return
            if y < 0 or y >= len(image[0]): return
            
            if image[x][y] == newColor: return
            if image[x][y] != start_color: return
            
            image[x][y] = newColor
            
            flood_fill(x-1, y)
            flood_fill(x+1, y)
            flood_fill(x, y+1)
            flood_fill(x, y-1)
        
        flood_fill(sr, sc)
        return image
