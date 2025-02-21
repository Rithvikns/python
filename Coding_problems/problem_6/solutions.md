# Complex University Management System

## Overview
This script simulates a **University Management System**, where set operations play a role in handling student enrollments. However, the system also includes other functionalities such as:
- Course assignments
- Student data processing
- Grading analytics

## Features
- **Student Enrollment Data:** Maintains sets of students enrolled in different courses.
- **Course Assignments:** Maps students to their enrolled courses.
- **Random Grade Assignment:** Assigns random grades between 50-100 to students for their courses.
- **Reports & Analytics:** Generates student reports and performs set operations to analyze enrollments.

---

## Code Explanation

### 1. **Data Initialization**
- **`math_students`**, **`science_students`**, and **`art_students`**: These sets store students enrolled in respective courses.
- **`all_courses`**: Stores all available courses.
- **`student_courses`**: A dictionary that maps students to their enrolled courses.

### 2. **`assign_random_grades()`**
- Iterates through `student_courses`, generating a random grade (50-100) for each course a student is enrolled in.
- Returns a dictionary containing student names and their corresponding grades per course.

**Example Output:**
```
{'Alice': {'Math': 76, 'Art': 89}, 'Bob': {'Math': 92}, ...}
```

### 3. **`generate_report(grades)`**
- Takes the generated grade dictionary and prints a structured report of students and their grades.

**Example Output:**
```
Student: Alice
  Math: 76
  Art: 89

Student: Bob
  Math: 92
```

### 4. **`analyze_student_data()`**
This function utilizes **set operations** to analyze student enrollments:
- **Union (`|`)**: Combines all students into `all_students`.
- **Intersection (`&`)**: Finds students enrolled in both Math and Science.
- **Difference (`-`)**: Identifies students in Math but not in Science.
- **Symmetric Difference (`^`)**: Finds students who are in either Math or Science but not both.
- **Subset Check (`issubset()`)**: Determines if Math students are a subset of all students.
- **Superset Check (`issuperset()`)**: Checks if `all_students` contains all Science students.
- **Disjoint Check (`isdisjoint()`)**: Verifies if Art and Science students are entirely separate.

**Example Output:**
```
All students: {'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'}
Students in both Math and Science: {'Charlie', 'David'}
Students in Math but not Science: {'Alice', 'Bob'}
Students in Math or Science but not both: {'Alice', 'Bob', 'Eve', 'Frank'}
Are all Math students in the total student list? True
Does all_students contain all Science students? True
Are Art and Science students completely separate? False
```

### 5. **Main Execution Block**
```python
if __name__ == "__main__":
    print("--- University Management System ---\n")
    student_grades = assign_random_grades()
    generate_report(student_grades)
    analyze_student_data()
```
- Calls functions to assign grades, generate reports, and analyze data when the script is executed.

---

## Conclusion
This script integrates **set operations** as part of a broader **University Management System**. It effectively demonstrates how **data manipulation, analytics, and operations on sets** can be used in real-world applications. 🚀

