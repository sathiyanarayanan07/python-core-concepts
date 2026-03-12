numbers = range(1,31)

for number in numbers:
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3== 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(f"{number}")
         