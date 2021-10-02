# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        
        
        lp =  0
        rp = n-1
        
        while lp<rp:
            mid = lp + (rp-lp)//2
            
            # we need to go the left
            if isBadVersion(mid):
                rp = mid - 1
            # we need to go to the right
            else:
                lp = mid + 1
                
        return lp if isBadVersion(lp) else lp + 1
                
        
