1️⃣ Writing to a file ("w" mode)
# Open a file in write mode ("w")
# If the file does not exist, Python creates it automatically.
# If the file already exists, its contents will be overwritten.
score_file = open("score.txt", "w", encoding="utf8")

# Write text to the file using print()
# file=score_file tells Python to write to the file instead of the console
print("Math : 0", file=score_file)
print("English : 50", file=score_file)

# Always close the file after writing
# This saves the data properly and releases system resources
score_file.close()

📄 Result in score.txt
Math : 0
English : 50

2️⃣ Appending to a file ("a" mode)
# Open the file in append mode ("a")
# This adds new content to the end of the file without deleting existing data
score_file = open("score.txt", "a", encoding="utf8")

# write() does NOT automatically add a newline
score_file.write("Science : 80")
score_file.write("\nCoding : 100")

score_file.close()

📄 Updated score.txt
Math : 0
English : 50
Science : 80
Coding : 100

3️⃣ Reading a file line by line with readline()
# Open the file in read mode ("r")
score_file = open("score.txt", "r", encoding="utf8")

# readline() reads one line at a time
# After reading a line, the cursor moves to the next line
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())

score_file.close()

🖥 Output
Math : 0

English : 50

Science : 80

Coding : 100

Blank lines appear because each line already ends with \n.

4️⃣ Reading a file using a while loop
score_file = open("score.txt", "r", encoding="utf8")

while True:
    line = score_file.readline()
    if not line:  # End of file
        break
    print(line)

score_file.close()

🖥 Output (same result)
Math : 0

English : 50

Science : 80

Coding : 100

5️⃣ Reading all lines at once with readlines()
score_file = open("score.txt", "r", encoding="utf8")

# readlines() returns a list of lines
lines = score_file.readlines()

for line in lines:
    # end="" prevents print() from adding an extra newline
    print(line, end="")

score_file.close()

🖥 Output
Math : 0
English : 50
Science : 80
Coding : 100
