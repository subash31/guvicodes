n=int(input())
k = int(input())
arr = []
sum = 0
for i in range(0,n):
    ele = int(input())
    arr.append(ele)
if (n>=k):
    for i in range(0,k):
        sum += arr[i]
else:
    sum = -1
print(sum)
