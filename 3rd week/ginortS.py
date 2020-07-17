

my_str = input()
sorted_str = sorted(my_str)

upper = []
lower = []
even = []
odd = []

def ginortS(x):
    if x.isalpha():
        if x.isupper():
            upper.append(x)
        else:
            lower.append(x)
    else:
        if int(x) % 2 == 0:
            even.append(x)
        else: 
            odd.append(x)

ginortS(my_str)

upper.sort()
lower.sort()
even.sort()
odd.sort()

t = lower + upper + odd + even
print(t)

#실패
#시간이 부족해 더 못해봤네요ㅠㅠ 
#이 코드에서 생기는 문제는, 'ginortS라는 함수를 대체 어떻게 적용시키는가'입니다. 원래 계획은 upper, lower, even, odd를 각각 만들고 input의 문자들을 적절히 집어넣은 뒤에 다시 합치는 것이었는데 쉽지 않네요..