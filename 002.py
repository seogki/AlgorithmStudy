n = int(input())
number = 0
numbers = []
for i in range(1,n + 1):
    result =  int(input())
    numbers.append(result)
    number += result

answer = number * 100 / max(numbers) / n

print(answer)