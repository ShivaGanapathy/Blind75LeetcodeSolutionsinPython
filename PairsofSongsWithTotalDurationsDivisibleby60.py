class Solution:
    #O(n^2) time brute force
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        output = 0
        for i in range(len(time)):
            for j in range(i+1,len(time)):
                if (time[i] + time[j])%60 == 0:
                    output += 1
        return output

    #O(n) time #O(n) space 
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hashmap = {}
        output = 0
        
        for item in time:
            item = item % 60
            complement = (60 - item) % 60
            
            if complement in hashmap:
                output += hashmap[complement]
                
            if item in hashmap:
                hashmap[item] +=1
            else:
                hashmap[item] = 1
                
        return output
                