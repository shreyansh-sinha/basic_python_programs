n = int(input())

arr = list(map(int, input().split()))
mx = max(arr)

sec_max = 0
for x in range(n):
    if arr[x] > sec_max and arr[x] != mx:
        sec_max = arr[x]

print(sec_max)

