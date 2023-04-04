# 나머지 합 구하기

numbers = [1,2,3,1,2]
hap = []
remains = [0] * 5
temp = 0
answer = 0
for i in range(0, 5):
    temp += numbers[i]
    hap.append(temp)
print(hap)
for i in range(0, 5):
    remainder = hap[i] % 3
    if remainder == 0:
        answer +=1
    remains[remainder] += 1

print(remains)

for i in range(3):
    answer += (remains[i] * (remains[i] - 1)//2)


print(answer)
