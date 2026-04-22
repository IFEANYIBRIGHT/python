from unittest import TestCase
import university_application


class MyTestCase(TestCase):

    def setUp(self):
         university_application.dict_for_each_student.clear()

         university_application.dict_for_each_student["STU001"] = {
            "Name": "John",
            "Age": 22,
            "Student Course": {"Math", "Physics"},
            "Student Address": {
                "Address": "Lagos",
                "Zip Code": "100001"
            }
        }

    def test_display_student_record(self):
        student = university_application.display_student_record("STU001")

        self.assertEqual(student["Name"], "John")

        self.assertEqual(university_application.display_student_record("001"),"Invalid ID format")

        self.assertEqual(university_application.display_student_record("STU999"),"Student not found")

    def test_display_courses(self):
        courses = university_application.display_courses("STU001")

        self.assertIn("Math", courses)
        self.assertIn("Physics", courses)

        self.assertEqual(university_application.display_courses("STU999"),"Student not found")

    def test_display_zip(self):
        address = university_application.display_zip("STU001")

        self.assertEqual(address["Zip Code"], "100001")

        self.assertEqual(
            university_application.display_zip("STU999"),
            "Student not found"
        )

    def test_total_students(self):
         self.assertEqual(len(university_application.dict_for_each_student),1)