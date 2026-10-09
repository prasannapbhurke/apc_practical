

with open("file.txt", "r") as f:
    text = f.read()


lines = text.count("\n")
words = len(text.split())
chars = len(text)


print("Lines:", lines)
print("Words:", words)
print("Characters:", chars)
