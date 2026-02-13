# Current Grade
from api.courses import grab_course_id, grab_course_name
import requests
import asyncio
import httpx
token = "7301~nRxEKy3m7Wa6HPxZM4PehVyL9DY3LGW6CwDJCEmtnBN4cM27GZ9LDacJU2w7LLGL"
url = "https://instructure.charlotte.edu/api/v1/courses"
headers = {"Authorization": f"Bearer {token}"}
params = {"per_page": 100,"user_id": "self"}

course_id = grab_course_id()
current_name = grab_course_name()
def grab_total_grades():
    """
    Grabbing each classes
    - name
    - course id
    - current grade
    """
    i = 0
    current = []
    while i < len(course_id):
        new_url = f"{url}/{course_id[i]}/enrollments"
        response = requests.get(new_url, headers=headers, params=params)
        if response.status_code != 200:
            return {"status code": response.status_code}
        else:
            data = response.json()
            for d in data:
                grades = d.get("grades", {})
                now = {
                    "course_id": d.get("course_id"),
                    "course_name": current_name[i],
                    "total_grade": grades.get("current_score")
                }
                current.append(now)
            i += 1
    return current
if __name__ == "__main__":
    print(grab_total_grades())


async def fetch_total_grades():
    async with httpx.AsyncClient(timeout=20) as client:
        total = []
        for i, cid in enumerate(course_id):
            new_url = f"{url}/{cid}/enrollments"
            response = await client.get(new_url, headers=headers, params=params)
            data = response.json()
            for d in data:
                grades = d.get("grades", {})
                grade = {
                    "course_id": cid,
                    "course_name": current_name[i],
                    "current_grade": grades.get("current_grade")
                }
                total.append(grade)
    return total

                

