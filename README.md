# README

## Overview

ReXus is a Django-based platform designed to streamline research project management and facilitate collaboration between faculty and students. The system provides features for managing research projects, scheduling meetings, tracking publications, and receiving automated notifications.

## Project Goals

- Efficiently manage research projects for faculty and students.
- Enable structured collaboration between researchers.
- Schedule and track meetings.
- Provide real-time notifications.
- Maintain a history of document revisions.
- Ensure scalability and seamless frontend-backend integration.

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

## Why ReXus? 

Managing research collaborations is complex, often replying on fragmented tools. ReXus automates & streamlines workflows:

- Faculty can manage research projects with ease.
- Students can request & join projects.
- Meetings can be scheduled & tracked.
- Notifications ensure timely updates.
- Document history is maintained for bettter tracking.

## Database Schema & ERDs

- ![ERD version 1](./Database-ERD-crows-foot-v1.png)

