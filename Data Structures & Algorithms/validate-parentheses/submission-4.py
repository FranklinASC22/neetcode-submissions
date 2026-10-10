class Solution:
    def isValid(self, s: str) -> bool:
        # Time: O(n) Space: O(n)
        #we want to remove correct pairs as we iterate through the string 
        hashmap = {")":"(","]":"[","}":"{"}
        stack = []

        for char in s:

            if char in hashmap: #checks that char in s is a closing parenthese
            #check that its a closing parenthese
                if stack and stack[-1] == hashmap[char]:
                #check that stack is not empty and make sure top
                #item in stack is the matching open parenthese
                    stack.pop() # remove open parenthese
                else: #wrong match or stack is empty
                    return False
            else: #if the char in s is an open parenthese
            #Add open parenthese to the stack
                stack.append(char)
        #can only return if stack is empty
        return True if not stack else False