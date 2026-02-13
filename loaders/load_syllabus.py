# loading syllabus into the database
from database.database import Syllabus

def upsert_syllabus(session, syllabus):
    for s in syllabus:
        existing = session.query(Syllabus).filter_by(course_id=s["course_id"]).one_or_none()
        if existing:
            existing.course_id = s["course_id"]
            existing.course_name = s["course_name"]
            existing.syllabus_text = s.get("syllabus_text")
        else:
            session.add(Syllabus(
                course_id = s["course_id"],
                course_name = s["course_name"],
                syllabus_text = s.get("syllabus_text")
            ))
        
    session.commit()