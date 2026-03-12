fruits = ["apple","banana", "apple", "cherry", "banana", "apple"]

fruit_count ={}

for fruit in fruits:
    if fruit in fruit_count:
        fruit_count[fruit] +=1
    else:
        fruit_count[fruit] =1


print(fruit_count)