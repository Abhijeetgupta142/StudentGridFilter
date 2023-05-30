from flask import Flask, jsonify, request
import csv

app = Flask(__name__)


def load_students():
    students = []
    with open('student_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students


@app.route('/students', methods=['GET'])
def get_students():
    students = load_students()

    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 5))

    total_students = len(students)

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    paginated_students = students[start_index:end_index]

    filter_id = request.args.get('id')
    filter_name = request.args.get('name')

    if filter_id:
        paginated_students = [student for student in paginated_students if student['id'] == filter_id]
    if filter_name:
        paginated_students = [student for student in paginated_students if student['name'].lower() == filter_name.lower()]

    response = {
        'page': page,
        'page_size': page_size,
        'total_students': total_students,
        'students': paginated_students
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
