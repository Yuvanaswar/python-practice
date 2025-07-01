total=0
for i in range(1,6):
    mark=int(input(f"Enter the mark{i}:"))
    total +=mark
average = total / 5

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Fail"

print("Total:", total)
print("Average:", average)
print("Grade:", grade)
