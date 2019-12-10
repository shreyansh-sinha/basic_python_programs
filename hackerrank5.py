n = int(input())
list = []

for x in range(n):
        z = int(input())
        list.append(z)

mx = 0
sec_max = 0;
for x in range(n):
    if list[x] > mx:
        mx = list[x]

for x in range(n):
    if list[x] > sec_max and list[x] != mx:
        sec_max = list[x]

print(sec_max)


