# Assignments
from api.courses import grab_course_id, grab_course_name
import requests
from bs4 import BeautifulSoup
import html
import os
from dotenv import load_dotenv
load_dotenv()


token = os.getenv("token")
url = "https://instructure.charlotte.edu/api/v1/courses"
headers = {"Authorization": f"Bearer {token}"}
params = {"per_page": 100, "include[]": ["assignment", "total_score", "submission_history"], "user_id": "self"}

course_id = grab_course_id()
course_name = grab_course_name()


def grab_assignments():
    """
    grab each student classes
    - assignment id
    - assignment name
    - assignment text
    - if submitted/submitted at
    - missing
    - late(True/False)
    - points deducted
    """
    i = 0
    assignments_data = []
    course_id = grab_course_id()
    while i < len(course_id):
        params = {"per_page": 100, "include[]": ["assignment", "total_score", "submission_history"]}
        new_url = f"{url}/{course_id[i]}/students/submissions"
        response = requests.get(new_url, headers=headers, params=params)
        if response.status_code != 200:
            return {"code": response.status_code}
        else:
            data = response.json()
            for d in data:
                # nested "assignment" object from include[]=assignment
                assignment_obj = d.get("assignment", {})
                # 🔹 1) RAW assignment description HTML (could be None)
                raw_html = assignment_obj.get("description") or ""
                # 🔹 2) Unescape HTML entities (\u003C, &amp;, etc.)
                unescaped = html.unescape(raw_html)
                # 🔹 3) Parse HTML and extract readable text
                soup = BeautifulSoup(unescaped, "html.parser")
                clean_text = soup.get_text(separator=" ", strip=True)
                assignments = {
                    "course_id": course_id[i],
                    "course_name": course_name[i],
                    "assignment_id": d.get("assignment_id"),
                    "assignment_name": assignment_obj.get("name"),
                    "assignment_text": clean_text if clean_text else None,
                    "submitted_at": d.get("submitted_at"),
                    "missing": d.get("missing"),
                    "late": d.get("late"),
                    "points_deducted": d.get("points_deducted")
                }
                assignments_data.append(assignments)
            i += 1
    return assignments_data
if __name__ == "__main__":
    print(grab_assignments())

    