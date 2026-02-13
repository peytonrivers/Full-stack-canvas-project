# Main file that runs everything into the database
# connect/main.py
import asyncio
import time
from database.database import init_db, get_session
from api.courses import grab_user_courses
from loaders.load_courses import upsert_courses
from api.grades import grab_grades
from loaders.load_grades import upsert_grades
from api.total_grades import grab_total_grades
from loaders.load_total_grades import upsert_total_grades
from api.modules import grab_modules
from loaders.load_modules import upsert_modules
from api.syllabus import grab_syllabus
from loaders.load_syllabus import upsert_syllabus
from api.assignments import grab_assignments
from loaders.load_assignments import upsert_assignments

def run_courses():
    session = get_session()
    try:
        courses = grab_user_courses()
        upsert_courses(session, courses)
        print("successfully loaded into database")
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()
    

def run_grades():
    session = get_session()
    try:
        grades = grab_grades()
        upsert_grades(session, grades)
        print("Successfully inserted grades into the database")
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()

def run_total_grades():
    session = get_session()
    try:
        total_grades = grab_total_grades()
        upsert_total_grades(session, total_grades)
        print("successfully inserted into the database")
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()

def run_modules():
    session = get_session()
    try:
        modules = grab_modules()
        upsert_modules(session, modules)
        print("Successfully inserted modules into the database")
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()

def run_syllabus():
    session = get_session()
    try:
        syllabus = grab_syllabus()
        upsert_syllabus(session, syllabus)
        print("successfully uploaded syllabus into the database")
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()

def run_assignments():
    session = get_session()
    try:
        assignments = grab_assignments()
        upsert_assignments(session, assignments)
        print("Successfully loaded assignments into the database")
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()

async def main():
    await asyncio.gather(
        run_assignments(),
        run_courses(),
        run_grades(),
        run_modules(),
        run_syllabus(),
        run_total_grades()
    )

if __name__ == "__main__":
    asyncio.run(main())

