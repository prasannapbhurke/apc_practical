books = ["Python","Java","C++"]
books.append("AI")
book = input("Search book: ")
print("Book Found" if book in books else "Not Found")
books.remove("Java")
print(books)
print("Total Books:", len(books))

