n = int(input("Enter no of semester: "))
subject_counts = []
for i in range(1, n + 1):
    count = int(input(f"Enter no of subjects in {i} semester: "))
    subject_counts.append(count)
max_marks = []
for i in range(1, n + 1):
    print(f"Marks obtained in semester {i}:")
    marks = []
    valid = True
    for j in range(subject_counts[i - 1]):
        mark = int(input())
        if mark < 0 or mark > 100:
            print("You have entered invalid mark.")
            valid = False
            break
        marks.append(mark)
    if valid:
        max_marks.append(max(marks))
    else:
        max_marks.append(None)
for i in range(1, n + 1):
    if max_marks[i - 1] is not None:
        print(f"Maximum mark in {i} semester:{max_marks[i - 1]}")