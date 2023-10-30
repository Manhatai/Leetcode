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
#        return x == x[::-1] #Pythons way to reverse a string



class Solution(object):  #Trzecia próba, wynik pozytywny bez przekształcania na string
    def isPalindrome(self, x):
        if x < 0 or (x != 0 and x % 10 == 0): #Jeśli x jest negatywny, lub x kończy się na zerze, liczba nie może być palindromem
            return False

        half = 0 #Zmienna "half" zawiera odwróconą połowę liczby
        while x > half: #Póki x jest większy niż połowa,
            half = (half * 10) + (x % 10) #Dla przykładu 1221, half = (0 * 10) + (1221 % 10) = 1, więc w half zapisuje się liczba 1
            x = x // 10 #Floor division dzieli liczbę do całości, pozostawiając 122 jako x

        return x == half or x == half // 10 #Jeśli half jest takie samo jak finalne x, lub half jest takie samo jak x


solution = Solution()
x = 1228221
print(solution.isPalindrome(x))