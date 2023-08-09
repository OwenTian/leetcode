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
        subArraySize = 0

    	# variable to hold the largest size
        largestSize = 0
		# variable to keep track of index in found subarray
        subArrayIndex = 0
        
        # boolean to determine if found sub array in while loop iteration
        foundSubArray = False
        
    	# loop through the array starting from 0, increment index by 1 
    	# each time. this loop is the outer loop.
        i = 0
        while i < len(nums) - 1:

    		# if the int at next index is one greater than int at the 
    		# current index:
            if nums[i] + 1 == nums[i+1]:
                
                # set the sub array size to 2 since we have 2 elements
                subArraySize = 2
                
                # set subArrayIndex to keep track of where we are in sub array,
                # add 2 since we're moving forward past the two elements we know
                subArrayIndex = i + 2
      
    			# check for continuation of the subarray via:
                while subArrayIndex < len(nums):
                    # if we're at an odd counter, check if current int is one 
                    # less than previous
                    if subArraySize % 2 != 0 and \
                    nums[subArrayIndex] == nums[subArrayIndex - 1] + 1:
                        # increment subArraySize and subArrayIndex and continue
                        subArraySize = subArraySize + 1
                        subArrayIndex = subArrayIndex + 1
                        foundSubArray = True
                        continue
                    
                    # if we're at an even counter, check if current int is one 
                    # more than previous
                    if subArraySize % 2 == 0 and \
                    nums[subArrayIndex] == nums[subArrayIndex - 1] - 1:
                        # increment subArraySize and subArrayIndex and continue
                        subArraySize = subArraySize + 1
                        subArrayIndex = subArrayIndex + 1
                        foundSubArray = True
                        continue
                        
                    # else break out of while loop
                    else:
                        foundSubArray = False
                        break

                                        
    			# reached end of sub array. record subArraySize if it's larger
                # than the previous largest size
                if subArraySize > largestSize:
                    largestSize = subArraySize
    			
            # if we found a sub array:
            # add subArraySize to outer loop index so we skip the 
            # subarray that we just went through, restarting outer loop 
            # at the last element of the subarray.
            # else: add 1 to outer loop index
            if foundSubArray:
                i = i + subArraySize
            else:
                i = i + 1

            # reset subArraySize and subArrayIndex to 0.
            subArraySize = 0
            subArrayIndex = 0

    	# return largest sub array size if it is nonzero, else return -1
        if largestSize > 0:
            return largestSize
        else:
            return -1
