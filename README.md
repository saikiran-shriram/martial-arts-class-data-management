# Martial Arts Class Data Management System

A full-stack database management system for tracking martial arts students, coaches, classes, attendance, and tournament participation — built as a DBMS course project, extended with a Flask web interface for real CRUD operations.

## Features
- Student (Martial Artist) management — add, view, delete
- Coach management with experience tracking
- Dojo/Class management linked to martial art styles and coaches
- Attendance tracking (composite key: student + class + date)
- Tournament participation records

## Tech Stack
- **Database:** MySQL
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS

## Database Design
7 relational tables with proper foreign key relationships:
- `Martial_Artist` — student records
- `Coach` — instructor records
- `Dojo_Class` — class/session records
- `Martial_Art_Style` — style reference data
- `Attendance` — weak entity, composite primary key (artist_id, class_id, date)
- `Tournament` — competition records
- `Participates_in` — student-tournament junction table

## Setup
1. Clone the repo
2. Import the SQL schema into MySQL
3. Update database credentials in `app.py`
4. `pip install -r requirements.txt`
5. `python app.py`
