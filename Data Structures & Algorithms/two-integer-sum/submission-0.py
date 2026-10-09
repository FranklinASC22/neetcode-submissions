class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # value: index
        for index,val in enumerate(nums):
            # index is the index, val is the value
            ''' enumerate() Returns indices and values of as
            pairs.
            Helpful for looping over indices 
            and values of a list simultaneously!'''
            diff = target - val
            # 2 = 9 - 7
            if diff in hashmap:
                #Example: get value 2, index which is zero
                #return [the index of 2 and index of val]
                return [hashmap[diff], index]
            #update hashmap
            hashmap[val] = index