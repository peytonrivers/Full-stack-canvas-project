# Courses
import requests
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("token")
url = "https://instructure.charlotte.edu/api/v1/courses"
headers = {"Authorization": f"Bearer {token}"}
params = {"per_page": 100, "include[]": ["syllabus_body", "total_scores", "term"]}

"""
- course id
- course code
- course name
- start at
- end at
"""

def grab_user_courses():
    """
    Fetch the user's active Canvas courses with term and grade metadeta.

    This function sends a GET request to the Canvas API and returns a list
    of course dictionaries, each containing the course ID, course code,
    course name, current grade, and term start/end dates.

    Returns:
        list[dict]: A list of courses where each item has the structure
            {
                "course_id": int,           # Canvas Course ID
                "course_code": str,         # Course code displayed by Canvas
                "course_name: str,          # Full course name
                "current": float | None,    # Current grade percentage
                "term_start": str | None,   # ISO timestamp (or None)
                "term_end": str | None,     # ISO timestamp (or None)
            }
        
            If the request fails:
                dict: {"status": <HTTP_STATUS_CODE>}
            
    Raises:
        None directly, but may raise exceptions if the response structure
        is unexpectedly missing required fields

    Example:
        >>> grab_user_courses()
        [
            {
                "course_id": 244951,
                "course_code": "202580-HIST-1575-008-15837",
                "course_name": "American Democracy",
                "current": 93.44,
                "term_start": "2025-08-11T05:00:00Z",
                "term_end": "2025-12-21T05:00:00z"
            }
        ]
    """
    courses_data = []
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return {"status": response.status_code}
    else:
        data = response.json()
        for d in data:
            enrollment = d.get("enrollments", {})[0]
            courses = {
                "course_id": d.get("id"),
                "course_name": d.get("name"),
                "course_code": d.get("course_code"),
                "current_grade": enrollment.get("computed_current_score"),
                "term_start": d.get("term", {}).get("start_at"),
                "term_end": d.get("term", {}).get("end_at"),
            }
            courses_data.append(courses)
        return courses_data
    

def grab_course_id():
    """
    grabs students
    - each course id
    """
    course_id = []
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return {"status": response.status_code}
    else:
        data = response.json()
        for d in data:
            course_id.append(d.get("id"))
        return course_id
    
def grab_course_name():
    """
    grabs students
    - each classes name
    """
    course_name = []
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return {"status code": response.status_code}
    else:
        data = response.json()
        for d in data:
            course_name.append(d.get("name"))
        return course_name
    
def grab_assignments_id():
    assignment_id = []
    course_id = grab_course_id()
    params = {"per_page": 100, "include[]": ["assignment", "total_score", "submission_history"]}
    new_url = f"{url}/{course_id[0]}/students/submissions"
    response = requests.get(new_url, headers=headers, params=params)
    data = response.json()
    for d in data:
        assignment_id.append(d.get("assignment_id"))
    return assignment_id

if __name__ == "__main__":
    print(grab_user_courses())

