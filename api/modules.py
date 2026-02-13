# modules
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
params = {"per_page": 100}

course_id = grab_course_id()
course_name = grab_course_name()

def grab_modules():
    """
    grab each students
    - course id
    - course name
    - module id
    - module name
    - position of module
    - total module items
    """
    i = 0
    modules_data = []
    while i < len(course_id):
        new_url = f"{url}/{course_id[i]}/modules"
        response = requests.get(new_url, headers=headers, params=params)
        if response.status_code != 200:
            return {"status code": response.status_code}
        else:
            data = response.json()
            for d in data:
                modules = {
                    "course_id": course_id[i],
                    "course_name": course_name[i],
                    "module_id": d.get("id"),
                    "module_name": d.get("name"),
                    "position": d.get("position"),
                    "total_items": d.get("items_count"),
                }
                modules_data.append(modules)
            i += 1
    return modules_data

if __name__ == "__main__":
    print(grab_modules())