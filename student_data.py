import csv


def create_student_csv():

    students = [
        {'id': 1, 'name': 'Farooq Ansari', 'total_marks': 85},
        {'id': 2, 'name': 'Rohan Singh', 'total_marks': 92},
        {'id': 3, 'name': 'Atanu Sadhu', 'total_marks': 78},
        {'id': 4, 'name': 'Abhijeet Gupta', 'total_marks': 90},
        {'id': 5, 'name': 'Anjali Kumari', 'total_marks': 80},
    ]

    path = 'student_data.csv'

    fieldnames = ['id', 'name', 'total_marks']

    with open(path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)


if __name__ == '__main__':
    create_student_csv()
