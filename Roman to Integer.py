x = input("Podaj liczbę w alfabecie rzymskim: ")
variable = 0
nums = {'I': 1, "V": 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

for i in range(len(x) - 1):
    if nums[x[i]] < (nums[x[i + 1]]):
        variable = variable - nums[x[i]]
    else:
        variable = variable + nums[x[i]]
print(variable + nums[x[-1]])