'''
Given an integer array nums and an integer k, 
return the number of pairs (i, j) where i < j such that 
|nums[i] - nums[j]| == k.
'''
class Solution:
    def countKDifference(nums: List[int], k: int) -> int:
        count = 0
        num_counts = {}
        
        for num in nums:
            count += num_counts.get(num - k, 0)  # Check if there is a pair with difference k
            count += num_counts.get(num + k, 0)  # Check if there is a pair with difference -k
            
            num_counts[num] = num_counts.get(num, 0) + 1  # Update the count of current number
        
        return count


