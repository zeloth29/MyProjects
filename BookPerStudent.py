Students = int(input("How many Students are there?\n"))
Books = int(input("How many books are there?\n"))
Divide = round(Students/Books, 0)
Spare = Students%Books
print("There are", Divide, "books per student")
print("There are", Spare, "spare")