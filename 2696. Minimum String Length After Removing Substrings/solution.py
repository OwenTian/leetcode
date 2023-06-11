# Minimum String Length After Removing Substrings

class Solution(object):
	# this method takes in a string s with length between 1 and 100 consisting of only uppercase English letters.
	# it removes any instances of "AB" or "CD", and returns the length of the resulting sting
	# removing one instance of "AB" or "CD" can create a new instance that needs to be removed
	def minLength(self, s):
		
	# declare a variable strlen for the string length outside of the loop and use it as the limit for the while
	strlen = len(s)
	
	# loop through the string
	i = 0
	while i < strlen:
		# check if each index + the next letter is equal to AB
		if s[i:i+2] == "AB" or s[i:i+2] == "CD":
			# in both if statements, if a match is found, cut those two characters out of the string and
			# reform as a new string
			s = s[:i] + s[i+2:]
			# since we cut out characters we decrement the length of the string
			strlen = strlen - 2
			# reset i to 0 so that we can start over from the beginning of the string to scan for more instances
			i = 0
			# jump to the next iteration of while, skipping incrementing the index at end of while
			continue
		# increment i for the while loop to move to the next string index
           	i = i + 1
		
        return strlen
