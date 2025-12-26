# Using continue and break in loops

absent = [2, 5]  # students who are absent
no_book = [7]    # student who forgot the book

for student in range(1, 11):  # students from 1 to 10
    if student in absent:
        continue
    elif student in no_book:
        print("Class is over today. Student {0}, follow me to the staff room.".format(student))
        break
    print("Student {0}, please read your book.".format(student))

🖥 Output
Student 1, please read your book.
Student 3, please read your book.
Student 4, please read your book.
Student 6, please read your book.
Class is over today. Student 7, follow me to the staff room.
