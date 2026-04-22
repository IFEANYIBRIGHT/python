dict_for_each_student = {}

def student_record_dictionary(student_id, student_name, student_address, student_courses, student_age, student_zipcode):
    dict_for_each_student[student_id] = {
        "Name": student_name,
        "Age": student_age,
        "Student Course": set(student_courses),
        "Student Address": {
            "Address": student_address,
            "Zip Code": student_zipcode
        }
    }

def display_student_record(student_id):
    if not student_id.startswith("STU"):
        return "Invalid ID format"

    if student_id in dict_for_each_student:
        return dict_for_each_student[student_id]

    return "Student not found"

def display_courses(student_id):
    if student_id in dict_for_each_student:
        return dict_for_each_student[student_id]["Student Course"]
    return "Student not found"

def display_zip(student_id):
    if student_id in dict_for_each_student:
        return dict_for_each_student[student_id]["Student Address"]
    return "Student not found"

def total_students():
    print("Total students:", len(dict_for_each_student))


def main():
    student_id = input("Enter Student ID: ")

    student_name = input("Enter student name: ")
    student_age = int(input("Enter student Age: "))
    student_course = input("Enter student course: ")
    student_address = input("Enter student address: ")
    student_zipcode = int(input("Enter Zip code: "))

    if not student_id.startswith("STU"):
        print("Invalid ID format")
        return

    student_record_dictionary(
        student_id,
        student_name,
        student_address,
        [student_course],
        student_age,
        student_zipcode
    )

    menu = """
    1: Show Student Record
    2: Display Student Course
    3: Student Address
    4:Total Students
    """
    print(menu)

    user_options = int(input("Choose option: "))

    if user_options == 1:
        student_records = input("Enter Student ID: ")
        print(display_student_record(student_records))

    elif user_options == 2:
        student_records = input("Enter Student ID: ")
        print(display_courses(student_records))

    elif user_options == 3:
        student_records = input("Enter Student ID: ")
        print(display_zip(student_records))

    elif user_options == 4:
        total_students()

    else:
        print("Invalid option")


# main()