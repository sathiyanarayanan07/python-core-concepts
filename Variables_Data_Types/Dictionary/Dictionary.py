user = {
    "name":"Alice",
    "age": 25,
    "email":"alice@example.com",
    "is_pro" :True
}

# Adding a new place of info
user["location"] = "New York"

#upadting an existing value
user["age"] = 26

# Deleting info
del user["email"]
print(user["name"])
print(user["age"])
print(user)