# template to load 
from database.database import Grades

def upsert_grades(session, grades: list[dict]):
    for g in grades:
        existing = session.query(Grades).filter_by(assignment_id=g["assignment_id"]).one_or_none()

        if existing:
            existing.course_id = g.get("course_id")
            existing.course_name = g.get("course_name")
            existing.assignment_id = g["assignment_id"]
            existing.assignment_name = g["assignment_name"]
            existing.points = g.get("points")
            existing.points_possible = g.get("points_possible")
            existing.percent = g.get("percent")
        else: 
            session.add(Grades(
                course_id = g.get("course_id"),
                course_name = g.get("course_name"),
                assignment_id = g["assignment_id"],
                assignment_name = g["assignment_name"],
                points = g.get("points"),
                points_possible = g.get("points_possible"),
                percent = g.get("percent")
            ))
        
    session.commit()