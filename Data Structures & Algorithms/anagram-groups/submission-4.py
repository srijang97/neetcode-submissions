class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def get_freq_arr(s):
            zeros = [0]*26
            for char in s:
                zeros[ord(char) - ord('a')] += 1
            return tuple(zeros)

        freqToStrs = {}

        for s in strs:
            freq = get_freq_arr(s)

            if freq in freqToStrs:
                freqToStrs[freq].append(s)
            else:
                freqToStrs[freq] = [s]

        return [v for k, v in freqToStrs.items()]
                
