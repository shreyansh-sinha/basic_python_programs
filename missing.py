arr = list(map(int, input().split()))

sum = 0
for i in range(len(arr)):
	sum += arr[i]

z = int(abs(n*(n+1)/2 - sum))
print(z)