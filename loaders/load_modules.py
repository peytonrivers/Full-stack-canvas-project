# load the modules.py file into the database
from database.database import Modules

def upsert_modules(session, modules):
    for m in modules:
        existing = session.query(Modules).filter_by(module_id=m["module_id"]).one_or_none()
        if existing:
            existing.course_id = m.get("course_id")
            existing.course_name = m.get("course_name")
            existing.module_id = m["module_id"]
            existing.module_name = m.get("module_name")
            existing.position = m.get("position")
            existing.total_items = m.get("total_items")
        else:
            session.add(Modules(
                course_id = m.get("course_id"),
                course_name = m.get("course_name"),
                module_id = m["module_id"],
                module_name = m.get("module_name"),
                position = m.get("position"),
                total_items = m.get("total_items")
            ))
    session.commit()