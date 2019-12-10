t = int(input())
arr = []
for _ in range(t):
    x = input().split()
    command = x[0]
    if command == 'append':
        arr.append(int(x[1]))
    elif command == 'print':
        print(arr)
    elif command == 'insert':
        arr.insert(int(x[1]), int(x[2]))
    elif command == 'reverse':
        arr = arr[::-1]
    elif command == 'pop':
        arr.pop()
    elif command == 'sort':
        arr.sort()
    elif command == 'remove':
        arr.remove(int(x[1]))
        
