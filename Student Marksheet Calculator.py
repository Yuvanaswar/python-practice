#Mini Project Start (Beginner)
#Project: Student Marksheet Calculator

m1=int(input("enter mark1:"))
m2=int(input("enter mark2:"))
m3=int(input("enter mark3:"))
total=m1+m2+m3
avg=total/3
if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 60:
    grade = "C"
else:
    grade = "Fail"
print("total",total)
print("avg",avg)
print("grade",grade)
