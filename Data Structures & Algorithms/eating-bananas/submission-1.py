import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_k  = max(piles)
        min_k  = math.ceil(sum(piles)/h)
    
        def get_n_hours(k):
            return sum([math.ceil(x/k) for x in piles])

        ans = float("inf")

        while min_k <= max_k:

            mid = (min_k + max_k)//2

            hours = get_n_hours(mid)
            if get_n_hours(mid) > h:
                min_k = mid + 1

            elif get_n_hours(mid) <= h:
                ans = min(ans, mid)
                max_k = mid - 1

        return ans