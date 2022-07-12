class Solution:
    def twoSum(self, numbers,target):
        left,right = 0,len(numbers)-1
        while (left<right):
            currentSum = numbers[left] + numbers[right]
            if currentSum == target:
                return left+1,right+1
            elif currentSum > target:
                right -= 1
            else:
                left += 1
            
        
