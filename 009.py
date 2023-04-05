# 슬라이딩 윈도우

# 문자열 A C G T
# A는 1개 이상 C 1개 이상 G 1개 이상 T 0개 이상
# 길이가 4라고 가정

checkList = [0] * 4
myList = [0] * 4
checkSecret = 0

def myadd(c):
    global checkList,myList,checkSecret
    if c == 'A':
        myList[0] +=1
        if myList[0] == checkList[0]:
            checkSecret +=1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(c):
    global checkList,myList,checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -=1
        myList[0] -=1
    if c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -=1
        myList[1] -=1
    if c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -=1
        myList[2] -=1
    if c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -=1
        myList[3] -=1

S,P = map(int,input().split())
Result = 0
A = list(input())
checkList = list(map(int, input().split()))

for i in range(4):
    if checkList[i] == 0:
        checkSecret +=1

for i in range(P):
    myadd(A[i])

print(checkList)

if checkSecret == 4:
    Result +=1

for i in range(P,S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        Result += 1

print(Result)