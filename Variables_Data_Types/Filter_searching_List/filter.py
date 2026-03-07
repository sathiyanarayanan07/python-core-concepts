print ("---Available Books ---")

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


for book in library:
    if book["available"] == True:
        print(f'{book['title']}by {book['author']}')
    else:
        print("checkout")