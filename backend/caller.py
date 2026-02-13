# the goal is to set this as our call place to 
from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database.database import SessionLocal
from database.database import Courses
from database.database import Modules
from database.database import TotalGrades
from database.database import Assignments
from database.database import Grades

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow specific origins
    allow_credentials=True, # Allows cookies/auth headers to be included in requests
    allow_methods=["*"], # Allows all methods like (GET, PUT, POST, DELETE, etc.)
    allow_headers=["*"] # Allows all headers
    )


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# grabbing each of my courses name and final grade
@app.get('/courses')
def test(db: Session=Depends(get_db)):
    courses = db.query(Courses).all()
    return [
        {"course name": c.course_name,
         "final grade": c.current_grade
         }
         for c in courses
    ]

@app.get('/modules')
def get_modules(db: Session=Depends(get_db)):
    modules = db.query(Modules).order_by(Modules.course_name).all()
    return [
        {
            "Course Name": m.course_name,
            "Module Name": m.module_name,
            "Module Position": m.position,
            "Total Items": m.total_items
        }
        for m in modules
    ]

@app.get('/totalgrades')
def get_grades(db: Session=Depends(get_db)):
    total_grades = db.query(TotalGrades).all()
    return [
        {
            "Course Name": t.course_name,
            "Total Grade": t.total_grade
        }
        for t in total_grades
    ]

@app.get('/assignments')
def get_assignments(db: Session=Depends(get_db)):
    assignments = db.query(Assignments).all()
    grades = db.query(Grades).all()
    return [
        {
            "Course Name": a.course_name,
            "Assignment ID": a.assignment_id,
            "Assignment Name": a.assignment_name,
        }
        for a in assignments
    ]

@app.get("/grades")
def get_grades(db: Session=Depends(get_db)):
    grades = db.query(Grades).all()
    return [
        {
            "Course Name": g.course_name,
            "Assignment Name": g.assignment_name,
            "Points Possible": g.points_possible,
            "Percent": g.percent,
        }
        for g in grades
    ]

@app.get("/assignments_with_grades")
def get_assignments_with_grades(db: Session = Depends(get_db)):
    rows = (
        db.query(
            Assignments.course_name,
            Assignments.assignment_id,
            Assignments.assignment_name,
            Assignments.submitted_at,
            Grades.points_possible,
            Grades.percent,
        )
        .join(Grades, Grades.assignment_id == Assignments.assignment_id)
        .all()
    )

    return [
        {
            "Course Name": course_name,
            "Assignment ID": assignment_id,
            "Assignment Name": assignment_name,
            "Due Date": submitted_at,
            "Points Possible": points_possible,
            "Percent": percent,
        }
        for (course_name, assignment_id, assignment_name, submitted_at, points_possible, percent) in rows
    ]