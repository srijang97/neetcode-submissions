from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        valList = self.hashMap[key]

        L, R = 0, len(valList) - 1

        if len(valList) == 0:
            return ""

        while L < R:

            mid = (L + R + 1)//2

            if valList[mid][1] <= timestamp:
                L = mid
            else:
                R = mid - 1
        
        if valList[L][1] <= timestamp:
            return valList[L][0]
        else:
            return ""


            




        
