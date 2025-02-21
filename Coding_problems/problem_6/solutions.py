"""
Complex University Management System
This script simulates a university management system where set operations play a role in handling student enrollments, but the system includes other functionalities such as course assignments, student data processing, and analytics.
"""

import random

# Sample Data: Students enrolled in different courses
math_students = {"Alice", "Bob", "Charlie", "David"}
science_students = {"Charlie", "David", "Eve", "Frank"}
art_students = {"Alice", "Eve", "Grace"}

all_courses = {"Math", "Science", "Art", "History", "Physics"}
student_courses = {
    "Alice": {"Math", "Art"},
    "Bob": {"Math"},
    "Charlie": {"Math", "Science"},
    "David": {"Math", "Science"},
    "Eve": {"Science", "Art"},
    "Frank": {"Science"},
    "Grace": {"Art"}
}

def assign_random_grades():
    grades = {}
    for student, courses in student_courses.items():
        grades[student] = {course: random.randint(50, 100) for course in courses}
    return grades

def generate_report(grades):
    for student, courses in grades.items():
        print(f"Student: {student}")
        for course, grade in courses.items():
            print(f"  {course}: {grade}")
        print("\n")

def analyze_student_data():
    print("Analyzing student enrollments...")
    all_students = math_students | science_students | art_students
    math_and_science = math_students & science_students
    math_not_science = math_students - science_students
    math_xor_science = math_students ^ science_students
    is_math_subset = math_students.issubset(all_students)
    is_all_superset = all_students.issuperset(science_students)
    is_art_science_disjoint = art_students.isdisjoint(science_students)

    print("All students:", all_students)
    print("Students in both Math and Science:", math_and_science)
    print("Students in Math but not Science:", math_not_science)
    print("Students in Math or Science but not both:", math_xor_science)
    print("Are all Math students in the total student list?", is_math_subset)
    print("Does all_students contain all Science students?", is_all_superset)
    print("Are Art and Science students completely separate?", is_art_science_disjoint)

if __name__ == "__main__":
    print("--- University Management System ---\n")
    student_grades = assign_random_grades()
    generate_report(student_grades)
    analyze_student_data()
