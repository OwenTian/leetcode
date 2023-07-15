class Solution:
    # Counts the number of beautiful pairs in a 0-indexed integer array called nums
    # where a pair of indices i and j is called beautiful when the first digit of 
    # nums[i] and the last digit of nums[j] are coprime and:
    # 0 <= i < j < nums.length
    # 2 <= nums.length <= 100
    # 1 <= nums[i] <= 9999
    # nums[i] is not divisible by 10
    def countBeautifulPairs(self, nums: List[int]) -> int:
        
        # initialize a counter that keeps track of how many beautiful pairs there are
        # loop through each index in the array
            # for each index's value, compare it with each larger index's value via:
            # gcd(first, last) where first = int(str(num)[0]) and last = num%10
            # if a beautiful pair is found (gcd(first, last) = 1), increment the counter by 1
        
        # return the counter after the loop has completed
