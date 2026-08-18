from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # result = []
        
        # for s in strs:
        #     str_counter = Counter(s)
        #     added = False

        #     for i, r in enumerate(result):

        #         if str_counter == Counter(r[0]):
        #             result[i] += [s]
        #             added = True
        #             break

        #     if added == False:
        #         result.append([s])

        # return result      

        result = defaultdict(list)

        for s in strs:

            chars = [0]*26

            for ch in s:
                chars[ord(ch)-ord('a')] += 1
            
            result[tuple(chars)] = result[tuple(chars)] +  [s]

        return list(result.values() )      

