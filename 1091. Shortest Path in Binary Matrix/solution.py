class Solution(object):
# Given an n x n binary matrix grid, we return the shortest clear path in 
# the matrix, or -1 for no clear path.

# A clear path is a path from the top-left cell to the bottom right cell
# such that:

	# 1. all visited cells are 0
	# 2. all adjacent cells are different and share an edge or corner

	def findAdjacent(grid: List[List[int]], start: Tuple[int, int]) -> List[Tuple[int, int]]:
	# Create method to find surrounding cells that are clear path, given a  
	# matrix and a current location.

		# Define directions as tuples (-1, 0), (1, 0), (0, -1), (0, 1), 
		# (-1, -1), (-1, 1), (1, -1), (1, 1), (-1, -1).
		directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1), (1, 1), (-1,-1)]
		clearPaths = []

		# For the given location, check if there are any 0's in the 8  
		# surrounding spots. Also check if any of these are out of bounds.
		for i in range(len(directions)):
			new_x = start[0] + directions[i][0]
			new_y = start[1] + directions[i][1]

			if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 0 :
				clearPaths.append(directions[i])

		# Return a list of the surrounding 0's
		return clearPaths


	def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
		# Initalize queue for BFS to keep track of which cells are waiting to be 
		# processed as queue = [(0,0)]. Tuples represent the difference between the
		# matrix location and the upper leftmost cell.
		queue = [[0,0]]

		# Initialize step counter variable
		step = 1

		# Get the width and height of the matrix
		gridWidth, gridHeight = len(grid), len(grid[0])

		# Check if we're starting with 0, if not, return -1
		if(grid[0][0] != 0):
			return -1

		# while queue is not empty
		while queue:
			# set numCellsThisRound to length of queue
			numCellsThisRound = len(queue)
			# iterate through i in range(numCellsThisRound)
			for i in range(numCellsThisRound):
				# set current node = pop the top cell off the queue
				currentCell = queue.pop(0)
				# For each node, if the node is the bottom right most cell, return  
				# the current step size because we have found the shortest path.
				if currentCell[0] == gridWidth-1 and currentCell[1] == gridHeight-1:
					return step
	
				# Else use above method to find surrounding 0's and add those to the
				# queue.
				
				else:
					adjacentZeros = Solution.findAdjacent(grid, currentCell)
					results = []
					# Loop through the tuples eg. (-1,0) which represent where adjacent
					# zeros are located relative to currentCell
					for i in range(len(adjacentZeros)):
						adjacentZerosTuple = adjacentZeros[i]
						y = currentCell[1] + adjacentZerosTuple[1]
						x = currentCell[0] + adjacentZerosTuple[0]
						queue.append(list((x,y)))
						grid[x][y] = -1
			step = step + 1

		# return -1 if there is no path
		return -1
