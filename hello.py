import sys

def read_students_csv(filename):
    try:
        f = file(filename)
        lines = [line.strip() for line in f.readlines()]

        return {
            'header': lines[0],
            'records': lines[1:],
        }

    except IOError:
        print filename, 'does not exist'
        sys.exit()

    except IndexError:
        print 'Oops, you tried to read an empty file.'
        sys.exit()


def make_student(s, header):
    headers = header.split(',')
    parts = s.split(',')

    try:
        return {
            headers[0]: parts[0],
            headers[1]: parts[1],
        }
    except IndexError:
        return None


def average_age(students):
    """
    [{'studentname': 'student1', 'studentage': '10'}, None, {'studentname': 'student3', 'studentage': '15'}]
    """

    total = 0
    sum_age = 0.0

    for student in students:
        if not student: continue
        sum_age = sum_age + int(student['studentage'])
        total = total + 1

    return sum_age / total


def main():
    students_csv = read_students_csv('students.csv')
    #print(students_csv['records'])

    # transform raw student records (which are strings) into student dictionaries
    students = [make_student(record, students_csv['header']) for record in students_csv['records']]
    #print students

    print average_age(students)


if __name__ == '__main__':
    main()
