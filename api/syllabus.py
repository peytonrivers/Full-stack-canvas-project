# syllabus
from api.courses import grab_course_id, grab_course_name
import requests
from bs4 import BeautifulSoup
import html
import os
from dotenv import load_dotenv

token = os.getenv("token")
url = "https://instructure.charlotte.edu/api/v1/courses"
headers = {"Authorization": f"Bearer {token}"}
params = {"per_page": 100, "include[]": "syllabus_body"}

course_id = grab_course_id()
course_name = grab_course_name()

def grab_syllabus():
    """
    grab students
    - course id
    - course name
    - syllabus text
    """
    i = 0
    syllabus_data = []
    while i < len(course_id):
        new_url = f"{url}/{course_id[i]}"
        response = requests.get(new_url, headers=headers, params=params)
        if response.status_code != 200:
            return {"status code": response.status_code}
        else:
            data = response.json()
            # grabbing and cleaning the syllabus text
            raw_html = data.get("syllabus_body") or ""
            unescaped = html.unescape(raw_html)
            soup = BeautifulSoup(unescaped, "html.parser")
            clean_text = soup.get_text(separator=" ", strip=True)

            syllabus = {
                "course_id": data.get("id"),
                "course_name": data.get("name"),
                "syllabus_text": clean_text
            }
            syllabus_data.append(syllabus)
            i += 1
    return syllabus_data

if __name__ == "__main__":
    print(grab_syllabus())