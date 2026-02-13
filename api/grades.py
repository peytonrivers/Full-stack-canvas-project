# grades
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
params = {"per_page": 100, "include[]": "assignment"}

course_id = grab_course_id()
print(course_id)
course_name = grab_course_name()

def grab_grades():
    """
    grabes each studnets classes
    - assignment id
    - assignment name
    - score
    - points possible
    - percent
    """
    i = 0
    grades_data = []
    while i < len(course_id):
        new_url = f"{url}/{course_id[i]}/students/submissions"
        response = requests.get(new_url, headers=headers, params=params)
        if response.status_code == 403:
            print(response.status_code)
            continue
        elif response.status_code != 200:
            return {"status code": response.status_code}
        else:
            data = response.json()
            for d in data:
                assignment_obj = d.get("assignment",{})
                score = d.get("score")
                points_possible = assignment_obj.get("points_possible")
                if score is not None and points_possible is not None and points_possible > 0:
                    percent = round((score / points_possible) * 100, 2)
                else:
                    percent = None
                grade = {
                    "course_id": course_id[i],
                    "course_name": course_name[i],
                    "assignment_id": d.get("assignment_id"),
                    "assignment_name": assignment_obj.get("name"),
                    "points": score,
                    "points_possible": points_possible,
                    "percent": percent
                }
                print(grade)
                grades_data.append(grade)
            i += 1
    return grades_data

if __name__ == "__main__":
    print(grab_grades())