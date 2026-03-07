library = [

     {
        "title": "psychology of money",
        "author": "Morgan Housel",
        "available": False
    },

    {
        "title":"Atomic Habits",
        "author": "James Clear",
        "available": True
    }
]

new_book = {
    "title": "Deep work",
    "author":"cal newport",
    "available": True
}

library.append(new_book)

library[0]["available"] = True

print(library)
