'''
Author : Alexis Rodriguez
Date : 27 June 2019

python lamda expressions practice

'''

## Lambda expression basic form --> lambda num: pow(num, 2)
myNums = [
    1,2,3,4,5,6,7,8,9,10
]
print("Squaring the numbers in myNums is equal to : " )
print(list(map(lambda num : pow(num, 2), myNums)))