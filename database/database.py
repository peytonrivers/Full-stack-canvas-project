#Canvas Database
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

username = "peytonrivers"
host = "localhost"
port = 5432
database_name = "canvas_db"
# creating the PostgreSQL engine
engine = create_engine(DATABASE_URL, echo=True)
# declaring the base that will allow me to set up table frames for database
Base = declarative_base()
# Create a session for working with the DB
SessionLocal = sessionmaker(bind=engine)

# Give me a database connection when I need one
def get_session():
    return SessionLocal()

# building the Assignment table
class Assignments(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key = True, autoincrement=True)
    course_id = Column(Integer, nullable=True)
    course_name = Column(Text)
    assignment_id = Column(Integer, unique=True, index=True, nullable=False)
    assignment_name = Column(String)
    assignment_text = Column(Text, nullable=True)
    submitted_at = Column(DateTime, nullable=True)
    missing = Column(Boolean, nullable=True)
    late = Column(Boolean, nullable=True)
    points_deducted = Column(Float, nullable=True)


# Create a session for working with the DB
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# building the Courses table
class Courses(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, unique=True, index=True, nullable=False)
    course_name = Column(String, nullable=False)
    course_code = Column(String, nullable=False)
    current_grade = Column(Float, nullable=True)
    term_start = Column(DateTime, nullable=True)
    term_end = Column(DateTime, nullable=True)

# building the Grades table
class Grades(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, nullable=True)
    course_name = Column(Integer, nullable=True)
    assignment_id = Column(Integer, unique=True, index=True, nullable=False)
    assignment_name = Column(String, nullable=False)
    points = Column(Float, nullable=True)
    points_possible = Column(Float, nullable=True)
    percent = Column(Float, nullable=True)

# building the Total_Grades table
class TotalGrades(Base):
    __tablename__ = "total_grades"
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String, nullable=True)
    course_id = Column(Integer, unique=True, index=True, nullable=False)
    total_grade = Column(Float, nullable=True)

# building the Modules table
class Modules(Base):
    __tablename__ = "modules"
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, nullable=True)
    course_name = Column(String, nullable=True)
    module_id = Column(Integer, unique=True, index=True, nullable=False)
    module_name = Column(String, nullable=True)
    position = Column(Integer, nullable=True)
    total_items = Column(Integer, nullable=True)

class Syllabus(Base):
    __tablename__ = "syllabus"
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, unique=True, index=True, nullable=False)
    course_name = Column(String, nullable=False)
    syllabus_text = Column(Text, nullable=True)

# Create tables in the database
def init_db():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()








