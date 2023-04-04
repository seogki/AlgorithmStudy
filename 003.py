numbers = [5,4,3,2,1]
hap = [0,5,9,12,14,15]
# 구간합 공식
# s[j] - s[i -1]

# 합 배열 공식
# s[j] = s[i-1] + A[i]

s,e = map(int, input().split())
# (hap[e] = 12) - (hap[1-1] = 0) = 12
print(hap[e] - hap[s-1])



