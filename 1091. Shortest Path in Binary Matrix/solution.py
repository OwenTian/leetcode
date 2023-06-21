class Solution(object):
	# Given an n x n binary matrix grid, we return the shortest clear path in 
	# the matrix, or -1 for no clear path.

	# A clear path is a path from the top-left cell to the bottom right cell
	# such that:

	 	# 1. all visited cells are 0
	 	# 2. all adjacent cells are different and share an edge or corner


	def findAdjacent(grid: List[List[int]], start_row: Tuple[int, int], start_col: Tuple[int, int]) -> List[Tuple[int, int]]:
		# Create method to find surrounding cells that are clear path, given a  
		# matrix and a current location.

			# Define directions as tuples (-1, 0), (1, 0), (0, -1), (0, 1), 
			# (-1, -1), (-1, 1), (1, -1), (1, 1).

			# For the given location, check if there are any 0's in the 8  
			# surrounding spots. Also check if any of these are out of bounds.

			# Return a list of the surrounding 0's


	def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
		# Initalize queue for BFS to keep track of which cells are waiting to be 
		# processed as queue = [(0,0)]. Tuples represent the difference between the
		# matrix location and the upper leftmost cell.
		# Initialize step counter variable

		# while queue is not empty
			
			# set numCellsThisRound to length of queue
			# iterate through i in range(numCellsThisRound)

				# set current node = pop the top cell off the queue
				# For each node, if the node is the bottom right most cell, return  
				# the current step size because we have found the shortest path.
	
				# Else use above method to find surrounding 0's and add those to the
				# queue.
	
				

			# step = step + 1

	  # return -1 if there is no path
