# 🎓 University Management System (Django REST Framework)

A role-based university management system built using **Django** and **Django REST Framework (DRF)**. This project enables effective academic data management for **students**, **faculty**, and **administrators** with secure authentication, role-based permissions, and RESTful APIs.

---

## 🔧 Features

- Custom user model with roles: Student, Faculty, Admin
- Role-based access for all models and views
- Full CRUD operations for:
  - Departments
  - Students & Teachers
  - Courses & Enrollments
  - Attendance & Timetable
  - Results & Withdrawals
- Throttling and pagination support
- Token-based authentication
- Admin panel integration

---

## 🏗️ Models Overview

### 1. `CustomUser`
- Extends `AbstractUser`
- Adds `user_type`: `student`, `faculty`, `admin`
- Linked to `Student` or `Teacher` via one-to-one relation

### 2. `Department`
- Academic departments (e.g., CS, Physics)

### 3. `Student`
- One-to-one with `CustomUser`
- Belongs to a department
- Has enrollments and results

### 4. `Teacher`
- One-to-one with `CustomUser`
- Belongs to a department
- Teaches courses

### 5. `Course`
- Has a name, code (e.g., CS101)
- Assigned to a faculty
- Linked to students via `Enrollment`

### 6. `Enrollment`
- Links student and course
- Records enrollment date

### 7. `Result`
- Stores grades for each student per course

### 8. `Attendance`
- Records attendance per student per course per date

### 9. `Withdrawal`
- Stores course withdrawal info

### 10. `Timetable`
- Course schedule (day, time, course)

---

## 🔁 Relationships Summary

| Entity        | Related To         | Relationship       |
|---------------|--------------------|--------------------|
| `CustomUser`  | `Student` / `Teacher` | One-to-One       |
| `Student`     | `Department`, `Course` | FK / M2M (via Enrollment) |
| `Teacher`     | `Department`, `Course` | FK               |
| `Course`      | `Teacher`, `Student`  | FK / M2M (via Enrollment) |
| `Result`      | `Student`, `Course`   | FK               |
| `Attendance`  | `Student`, `Course`   | FK               |
| `Withdrawal`  | `Student`, `Course`   | FK               |
| `Timetable`   | `Course`              | FK               |

---

## 🔐 Permissions & Authentication

### Role-Based Querysets:
Each `ViewSet` filters queryset based on the logged-in user's role:
- `Student`: Access only their data
- `Faculty`: Access related students & their own courses
- `Admin`: Full access

### Permissions:
```python
'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.DjangoModelPermissions',
]
