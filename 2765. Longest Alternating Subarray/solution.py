class Solution:

	# given a 0-indexed int array, find the maximum length alternating subarray
	# where:
	
	# 1. alternating means the subarray goes [x, x+1, x, x+1...] for the 
	# entire subarray
	# 2. the array is between 2 and 100 in length
	# 3. ints in the array are equal to or between 1 and 10^4
    def alternatingSubarray(self, nums: List[int]) -> int:

    	# declare a subArraySize variable that keeps track of length of 
    	# alternating subarrays.

    	# declare a list to hold potential subArraySizes.

    	# loop through the array starting from 0, increment index by 1 
    	# each time. this loop is the outer loop.

    		# if the int at next index is one greater than int at the 
    		# current index:

    			# set subArraySize = 2 since we have an alternating subarray 
    			# pair.

    			# create a new variable subArrayIndex and set that equal to the 
    			# current outer loop index + 1.

    			# check for continuation of the subarray via:

    			# while current value (at subArrayIndex) - 1 = next value and 
    			# current value = next next value and subArrayIndex 
    			# (the current index) is less than length of nums - 2:

    				# increment subArraySize by 2
    				# increment subArrayIndex by 2
    			
    			# reached end of sub array. append subArraySize to the list of 
    			# subArraySizes.
    			
    			# add subArraySize - 1 to outer loop index so we skip the 
    			# subarray that we just went through, restarting outer loop 
    			# at the last element of the subarray.

    			# reset subArraySize to 0.


    	# now that we have all possible subArraySizes, find biggest in the list 
    	# and return it.
