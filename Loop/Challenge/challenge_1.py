numbers = [ 1,2,3,4,5 ]

for i in numbers:
    if i == 3:
        print("skipping number 3")
        continue

    if i == 4:
        print("stop")
        break

    print(i)

