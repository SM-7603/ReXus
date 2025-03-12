# README

## Overview

ReXus is a Django-based platform designed to streamline research project management and facilitate collaboration between faculty and students. The system provides features for managing research projects, scheduling meetings, tracking publications, and receiving automated notifications.

## Why ReXus? 

Managing research collaborations is complex, often replying on fragmented tools. ReXus automates & streamlines workflows:

- Faculty can manage research projects with ease.
- Students can request & join projects.
- Meetings can be scheduled & tracked.
- Notifications ensure timely updates.
- Document history is maintained for bettter tracking.

---

## Project Goals

- Efficiently manage research projects for faculty and students.
- Enable structured collaboration between researchers.
- Schedule and track meetings.
- Provide real-time notifications.
- Maintain a history of document revisions.
- Ensure scalability and seamless frontend-backend integration.

---

## Setup Guide:

### 1 - Install Dependencies

```bash
pip install -r requirements.txt
```

### 2 - Run Django Server

```bash
python manage.py runserver
```

Access the server at `http://127.0.0.1:8000`

### 3 - How to interact with the database?

- Django Shell: `python manage.py shell` (interact with the models)
- PostgreSQL Shell: `python manage.py dbshell` (for direct queries)

---

## Database Schema & ERDs

- ![ERD version 1](./Database-ERD-crows-foot-v1.png)
    - ERD v1
- ![ERD version 2](./ERD-v2.png)
    - ERD v2

---

## API Testing & Expected Results

---

### Authentication

#### Registering users

- Expected: User should be registered with ID, username, role, email & date_joined
- Actual: Successful registration

```bash
curl -X POST http://127.0.0.1:8000/api/users/register/ \
-H "Content-Type: application/json" \
-d '{
    "username": "faculty1",
    "password": "testpassword",
    "role": "faculty",
    "email": "faculty1@example.com"
}'
```

```bash
{
  "id": 1,
  "username": "faculty1",
  "email": "faculty1@example.com",
  "role": "faculty",
  "profile_pic": null,
  "date_joined": "2025-02-26T15:01:05.444099Z"
}
```

#### User Login (JWT Auth)

- Expected: JWT `access` & `refresh` tokens should be returned.
- Actual: Successful Authentication -> login

```bash
curl -X POST http://127.0.0.1:8000/api/users/login/ \
-H "Content-Type: application/json" \
-d '{
    "username": "faculty1",
    "password": "testpassword"
}'
```

```bash
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0MTE4NzIzMiwiaWF0IjoxNzQwNTgyNDMyLCJqdGkiOiIzMDI3YjQxMTVjYzU0ZGVlYTU0MmIxNDIzODQzYWUwOCIsInVzZXJfaWQiOjF9.1p3K5F-CDQVlvEiGgw6WQZYSsnLkVvmP5LbRpeCpZb0",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQwNTg2MDMyLCJpYXQiOjE3NDA1ODI0MzIsImp0aSI6IjNiMzU2ZWIzY2Q4ZjRmYWU5MDBlYzM2NmUyMjE2ZDg2IiwidXNlcl9pZCI6MX0.ogmMIpuJPF-_AIooFx-cYD9JsjmNG8mvOKo5FzgK9kQ",
  "user": {
    "id": 1,
    "username": "faculty1",
    "email": "faculty1@example.com",
    "role": "faculty",
    "profile_pic": null,
    "date_joined": "2025-02-26T15:01:05.444099Z"
  }
}
```

---

### Project Management

#### Creating a research project

- Expected: Project should be created successfully.
- Acutal: Project creation works!

```bash
curl -X POST http://127.0.0.1:8000/api/projects/ \
-H "Authorization: Bearer $TOKEN" \
-H "Content-Type: application/json" \
-d '{
    "title": "AI Research",
    "description": "Exploring deep learning applications.",
    "status": "active"
}'
```

```bash
{
  "id": 1,
  "title": "AI Research",
  "description": "Exploring deep learning applications.",
  "faculty": "faculty1 (faculty)",
  "students": [],
  "start_date": "2025-02-26",
  "end_date": null,
  "status": "active"
}
```

#### Assigning students to a project

- Expected: Students should be assigned successfully.
- Actual: Students successfully added to project!

```bash
curl -X POST http://127.0.0.1:8000/api/projects/1/assign-student/ \
-H "Authorization: Bearer $TOKEN" \
-H "Content-Type: application/json" \
-d '{
    "student_id": 3
}'
```

```bash
{
  "message": "Student assigned successfully"
}
```

#### View all projects

- Expected: Should return a list of projects with the assigned students respectively.
- Acutal: works as expected.

```bash
curl -X GET http://127.0.0.1:8000/api/projects/ \
-H "Authorization: Bearer $TOKEN"
```

```bash
[
  {
    "id": 1,
    "title": "AI Research",
    "description": "Exploring deep learning applications.",
    "faculty": "faculty1 (faculty)",
    "students": [
      {
        "id": 3,
        "username": "student2",
        "email": "student2@example.com"
      }
    ],
    "start_date": "2025-02-26",
    "end_date": null,
    "status": "active"
  }
]
```

#### Create a project without the required fields (*this should fail*)

- Expected: should return an error -> missing required fields.
- Actual: error handled correctly.

```bash
curl -X POST http://127.0.0.1:8000/api/projects/ \
-H "Authorization: Bearer $TOKEN"
```

- result:

```bash
{
  "title": [
    "This field is required."
  ],
  "description": [
    "This field is required."
  ]
}
```

---

## [ ] TODO: 2025-02-27

### Meeting Management API

#### Requesting a meeting

#### Approving / Rejecting a meeting

##### Approving a meeting

##### Rejecting a meeting

#### Handling Invalid requests

##### Requesting a meeting with a faculty that doesn't exist

##### Sending an invalid JSON request

---

## Changelog (feature, improvement & fixes summary)

### 2025-02-27

- Meeting API
    - Added meeting request api.
    - Faculty can now approve / reject meeting requests.
    - Students can only see **their own** meetings, whilst faculties can view all the meetings they oversee.
    - Clearer error messages have been written.
- Validation Improvements
    - Bad JSON requests return detailed paring errors.
    - Meetings can't be scheduled without selecting a faculty.
- Security 
    - **Only students** can request meetings.
    - **Only faculty** can approve / reject meetings.

### 2025-02-26

- Fixed Password Hashing Issue
    - Passwords are now securely hashed during registration.
- Resolved Authentication Issues
    - Login failures were fixed by ensuring credentials match the hashed passwords.
- Project Management Fixes
    - Confirmed that students can be assigned to projects.
    - Fixed API responses to show full student details instead of just IDs.
- Validation Improvements
    - Missing fields now return meaningful error messages.
