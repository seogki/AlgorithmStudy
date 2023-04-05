# 두가지 재료의 합으로 만들수있음

# 6개의 재료 9개의 번호합
# 가지고있는 재료 숫자
# 2 7 4 1 5 3

numbers = sorted([2,7,4,1,5,3])
print(numbers)

sum = 0
i = 0
j = len(numbers) - 1
count = 0
maxNum = 9
while i < j:
    sum = numbers[i] + numbers[j]
    if sum < maxNum:
        i += 1
    elif sum > maxNum:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1


print(count)




