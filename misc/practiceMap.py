def square(num):
    return pow(num, 2)

getList = [int(x) for x in str(input("Enter numbers : ")).split(' ')]
print("Squaring the numbers provided : ", list(map(square, getList)))
