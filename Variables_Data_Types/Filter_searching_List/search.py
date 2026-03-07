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

search_query = "psychology of money"

print(f"\nsearching for books by: {search_query}")

for book in library:
    if search_query.lower() in book["title"].lower():
        status = "available" if book["available"] else "checkout"
        print(f"Result: {book['title']} [{status}]")

