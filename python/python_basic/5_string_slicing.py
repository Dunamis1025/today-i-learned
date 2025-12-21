# String Slicing Example

personal_id = "900101-1234567"

print("Gender code: " + personal_id[7])
print("Year: " + personal_id[0:2])
print("Month: " + personal_id[2:4])
print("Day: " + personal_id[4:6])


print("Date of birth: " + personal_id[:6])
print("Last 7 digits: " + personal_id[7:])
print("Last 7 digits (from the end): " + personal_id[-7:])
