class Solution:

    # Counts the number of beautiful pairs in a 0-indexed 
    # integer array called nums where a pair of indices i and j is
    # called beautiful when the first digit of 
    # nums[i] and the last digit of nums[j] are coprime and:
    # a) 0 <= i < j < nums.length
    # b) 2 <= nums.length <= 100
    # c) 1 <= nums[i] <= 9999
    # d) nums[i] is not divisible by 10
    def countBeautifulPairs(self, nums: List[int]) -> int:

        # initialize a counter that keeps track of how many 
        # beautiful pairs there are
        counter = 0

        # loop through the list of numbers and convert into a list of tuples 
        # that contain the first and last digits of each number
        listOfFirstLast = []
        for i in range(len(nums)):

            # isolate the first digit by converting the num into a  
            # string and grabbing the first char (which is the first digit)
            # via [0], then convert back into an int
            firstDigit = int(str(nums[i])[0])
            
            # isolate the last digit by using num % 10, the remainder 
            # will be the last digit
            lastDigit = nums[i]%10
        
            listOfFirstLast.append((firstDigit, lastDigit))

        # loop through each index in the list of first/last tuples:
        for i in range(len(listOfFirstLast)):
                
            # for each index's value, compare it with each larger 
            # index's value via: gcd(first, last)
            for j in range(i+1, len(listOfFirstLast)):
                
                first = listOfFirstLast[i][0]
                last = listOfFirstLast[j][1]

                # if a beautiful pair is found (gcd(first, last) = 1)
                # increment the counter by 1
                if gcd(first, last) == 1:
                    counter = counter + 1
                       
        # return the counter after the loop has completed
        return counter
