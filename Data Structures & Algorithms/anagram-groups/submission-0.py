from typing import List
class Solution:
    def groupAnagrams(self,strs:List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            sorted_word = sorted(word)
            key = ""
            for char in sorted_word:
                key = key+char
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        result = []
        for value in groups.values():
            result.append(value) 
        return result             

