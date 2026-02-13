# Load courses.py file into the database
from dateutil.parser import isoparse
from database.database import Courses


def to_datetime(value):
    return isoparse(value) if value else None


def upsert_courses(session, courses: list[dict]):
    for c in courses:
        existing = session.query(Courses).filter_by(course_id=c["course_id"]).one_or_none()

        if existing:
            existing.course_id=c["course_id"]
            existing.course_name = c["course_name"]
            existing.course_code = c["course_code"]
            existing.current_grade = c.get("current_grade")
            existing.term_start = to_datetime(c.get("term_start"))
            existing.term_end = to_datetime(c.get("term_end"))
        else:
            session.add(Courses(
                course_id=c["course_id"],
                course_name=c["course_name"],
                course_code=c["course_code"],
                current_grade=c.get("current_grade"),
                term_start=to_datetime(c.get("term_start")),
                term_end=to_datetime(c.get("term_end")),
            ))

    session.commit()

