secret_password = "python123"

data = input("Enter your secret passowrd: ")

if secret_password == data:
    print("Access Granted!")
else:
    print("Access Denied")