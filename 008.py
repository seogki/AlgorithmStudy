# 좋은수 구하기

numbers = [1,2,3,4,5,6,7,8,9,10]


result = 0
count = 0
index = 0
for k in range(len(numbers)):
    find = numbers[k]
    i = 0
    j = len(numbers) - 1
    while i < j:
        res = numbers[i] + numbers[j]
        if res == find:
            if i != k and j != k:
                count+=1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif res < find:
            i+=1
        else:
            j-=1

print(count)