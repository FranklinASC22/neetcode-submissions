class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        1. Remove non alphanumeric characters and spaces
        2. Convert all alphanumeric characters to lower case using <char>.lower()
        Note: to convert to upper case is <char>.upper()
        3. Reverse the string then check if its still equal

        *Use ASCII values to help skip non-alphanumeric characters*
        ord() gives you the ascii values
        '''
        left = 0
        right = len(s) - 1
        
        while(left < right):

            '''
            The reason you use self.check_alphanum() is that it
            is a method belonging to your Solution class, and self lets you 
            access methods and attributes belonging to the current object -> Class Solution.
            '''
            #check that chars are alphanumeric
            while left < right and not self.check_alphanum(s[left]):
                left += 1 #skips non-alphanumeric chars
            while right > left and not self.check_alphanum(s[right]):
                right -= 1 #skips non-alphanumeric chars
            #compare the two chars at either end of the string
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1 

        return True
    
    def check_alphanum(self, c):

        return  (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

