class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        
        gridCopy = grid;
        
     
        numberOfIslands = 0;
        
        
        for i in range( len(grid)  ):
            for j in range(len(grid[0] )):
               #attempt to "sink" the current index of the grid
                numberOfIslands += self.sink(gridCopy, i, j);
       
      
        
        #return the total number of islands
        return numberOfIslands;
    
    
    
    def sink(self, grid,   i,  j) :
            
            
      
        if(i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])  or grid[i][j] == '0') :
            return 0;
       
        
       #set current index to 0
        grid[i][j] = '0';
        
        # sink all neighbors of current index
        self.sink(grid, i + 1, j);
        self.sink(grid, i - 1, j);
        self.sink(grid, i, j + 1);
        self.sink(grid, i, j - 1);
        
       #increment number of islands
        return 1;
