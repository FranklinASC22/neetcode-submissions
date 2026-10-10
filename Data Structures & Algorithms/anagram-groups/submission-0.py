class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #key -> character counts , value -> lists of anagrams for that sequence of char counts
        #to handle edge case if counts don't exist yet
        hashmap = defaultdict(list) 

        for word in strs:
            #array of 26 zeros
            count = [0] * 26 # a-z
           
            for char in word:
                # map 'a' to index 0 and 'z' to index 25
                count[ord(char) - ord("a")] += 1 
                #lists can't be keys in python so use tuples
                #group words with a particular char count together
            hashmap[tuple(count)].append(word) 
        return list(hashmap.values()) # change dictionary view {:} to list view [[]]