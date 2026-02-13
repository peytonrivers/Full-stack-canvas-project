# loading assignments.py file into the database
from dateutil.parser import isoparse
from database.database import Assignments

def to_datetime(value):
    return isoparse(value) if value else None

def upsert_assignments(session, assignments):
    for a in assignments:
        existing = session.query(Assignments).filter_by(assignment_id=a["assignment_id"]).one_or_none()
        if existing:
            existing.course_id = a.get("course_id")
            existing.course_name = a.get("course_name")
            existing.assignment_id = a["assignment_id"]
            existing.assignment_name = a["assignment_name"]
            existing.assignment_text = a.get("assignment_text")
            existing.submitted_at = to_datetime(a.get("submitted_at"))
            existing.missing = a.get("missing")
            existing.late = a.get("late")
            existing.points_deducted = a.get("points_deducted")
        else:
            session.add(Assignments(
                course_id = a.get("course_id"),
                course_name = a.get("course_name"),
                assignment_id = a["assignment_id"],
                assignment_name = a["assignment_name"],
                assignment_text = a.get("assignment_text"),
                submitted_at = to_datetime(a.get("submitted_at")),
                missing = a.get("missing"),
                late = a.get("late"),
                points_deducted = a.get("points_deducted")
            ))
    session.commit()