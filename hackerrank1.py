x = int(input())
if x%2 != 0:
    print("Weird")
elif x%2 == 0:
    if 2<=x<=5:
        print("Not Weird")
    elif 6<=x<=20:
        print("Weird")
    else:
        print("Not Weird")
