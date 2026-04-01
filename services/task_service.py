from database.connection import get_session
from models.task import Task

def create_task(user_phone, title, category="Geral"):
    session = get_session()
    try:
        new_task = Task(user_phone=user_phone, title=title, category=category)
        session.add(new_task)
        session.commit()
        session.refresh(new_task)
        return new_task
    finally:
        session.close()

def get_pending_tasks(user_phone):
    session = get_session()
    try:
        tasks = session.query(Task).filter(
            Task.user_phone == user_phone,
            not Task.is_completed
        ).all()
        return tasks
    finally:
        session.close()

def complete_task(task_id, user_phone):
    session = get_session()
    try:
        task = session.query(Task).filter(
            Task.id == task_id, 
            Task.user_phone == user_phone
        ).first()
        
        if task:
            task.is_completed = True
            session.commit()
            return True
        return False
    finally:
        session.close()

def get_all_tasks_for_user(user_phone):
    session = get_session()
    try:
        tasks = session.query(Task).filter(
            Task.user_phone == user_phone
        ).all()
        return tasks
    finally:
        session.close()

def delete_task(task_id, user_phone):
    session = get_session()
    try:
        task = session.query(Task).filter(
            Task.id == task_id, 
            Task.user_phone == user_phone
        ).first()
        
        if task:
            session.delete(task)
            session.commit()
            return True
        return False
    finally:
        session.close()
