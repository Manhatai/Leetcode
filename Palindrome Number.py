#9. Palindrome Number
#class Solution(object):   Oryginalna próba, działa lecz kod jest zbyt wolny (pewnie ze względu na pętle while?)
#    def isPalindrome(self, x):
#        reversed = 0
#        original = x
#        while x != 0:
#           modulus = x % 10
#           reversed = reversed * 10 + modulus
#           x //= 10
#        y = reversed
#        return bool(y == original)



#class Solution(object):        Druga próba, wynik pozytywny lecz nie można konwertować int na str
#    def isPalindrome(self, x):
#        x = str(x)
#        return x == x[::-1]



class Solution(object):  #Trzecia próba, wynik pozytywny
    def isPalindrome(self, x):
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        half = 0
        while x > half:
            half = (half * 10)


solution = Solution()
x = 121
print(solution.isPalindrome(x))