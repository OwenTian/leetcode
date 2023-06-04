# Minimum String Length After Removing Substrings

# this method takes in a string s with length between 1 and 100 consisting of only uppercase English letters, removes any instances of "AB" or "CD", and returns the length of the resulting sting

# declare a variable strlen for the string length outside of the loop but use it as the limit for the loop
# loop through the string while incrementing by 1 with strlen - 1 as the ending
	# inner loop through the whole string, check if each index + the next letter is equal to AB
	# second inner loop check if each index + the next letter is equal to CD
		# in both loops, if a match is found, cut those two characters out of the string and reform as a new string
			# if this happens decrement strlen by 2
  # return strlen after the loops have finished

# trying to make a PR
