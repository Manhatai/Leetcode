#1. Two sum
class Solution(object):
    def twoSum(self, nums, target):
        list2 = {}                          #dict zawierający numery jako klucze i ich indeksy jako value
        for i, num in enumerate(nums):      #funkcja enumerate bierze z listy "nums": i jako indeks oraz num jako numer
            pozostały = target - nums[i]      #pozostały to wartość pozostała z odjęcia liczby o indeksie i od targetu
            if pozostały in list2:            #jeżeli pozostały znajduje się w list2:
                print(i)
                print(list2)
                print([i, list2[pozostały]])
                return [i, list2[pozostały]]  #zwraca indeks liczby poprzedniej i indeks liczby pozostały,
            else:                           #lub
                list2[num] = i              #dodaje liczbę do dicta jako indeks, sprawdzając kolejną liczbę


#asd
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))