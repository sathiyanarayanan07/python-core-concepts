data =["10","20","30","Apple","40","50"]

clean_numbers = []
for item in data:
    try:
        log= int(item)
        clean_numbers.append(log)
    except ValueError:
        print("skipping apple word!")

# write clean numbers into file

with open("clean_data.txt", "w") as file:
    for number in clean_numbers:
        file.write(str(number) + "\n") 