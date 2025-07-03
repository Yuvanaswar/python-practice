def get_marks():
    marks = []
    for i in range(5):
        mark = int(input(f"Enter mark {i+1}: "))
        marks.append(mark)
    return marks

def display_results(marks):
    print("Marks:", marks)
    total = sum(marks)
    avg = total / len(marks)
    print("Total:", total)
    print("Average:", avg)
    if avg >= 90:
        print("Grade: A")
    elif avg >= 75:
        print("Grade: B")
    elif avg >= 60:
        print("Grade: C")
    else:
        print("Grade: Fail")

marks = get_marks()
display_results(marks)

