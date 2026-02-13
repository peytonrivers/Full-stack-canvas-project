# loading total_grades.py file into the database
from database.database import TotalGrades

def upsert_total_grades(session, total_grades):
    for t in total_grades:
        existing = session.query(TotalGrades).filter_by(course_name=t["course_name"]).one_or_none()

        if existing:
            existing.course_name = t["course_name"]
            existing.course_id = t["course_id"]
            existing.total_grade = t.get("total_grade")
        else:
            session.add(TotalGrades(
                course_name = t["course_name"],
                course_id = t["course_id"],
                total_grade = t.get("total_grade")
            ))
    session.commit()