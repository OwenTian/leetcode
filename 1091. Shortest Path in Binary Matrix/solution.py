class Solution(object):
	# Given an n x n binary matrix grid, we return the shortest clear path in 
	# the matrix, or -1 for no clear path

	# A clear path is a path from the top-left cell to the bottom right cell
	# such that:

	 	# 1. all visited cells are 0
	 	# 2. all adjacent cells are different and share an edge or corner


	def findAdjacent(matrix, start_row, start_col):
		# create method to find surrounding cells that are clear path, given a  
		# matrix and a current location

			# define directions as tuples (-1, 0), (1, 0), (0, -1), (0, 1), 
			# (-1, -1), (-1, 1), (1, -1), (1, 1)

			# for the given location, check if there are any 0's in the 8  
			# surrounding spots, check if any of these are out of bounds

			# return a list of the surrounding 0's


	def shortestPathBinaryMatrix(self, grid):
		# initalize queue for BFS to keep track of which cells are waiting to be 
		# processed initialize step counter variable

		# while queue is not empty
			# iterate through nodes in the queue

			# for each node, if the node is the bottom right most cell, return  
			# the current step size because we have found the shortest path

			# else use above method to find surrounding 0's, add those to the
			# queue 

			# remove the first node from the queue

			# step = step + 1

	  # return -1 if there is no path
