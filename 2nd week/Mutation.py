first = input()
second = input()
num = int(second[0])
if num >= len(first):
    print("The number you gave is too large!")
else:
    print(first[:num] + second[2] + first[num+1:])

#성공