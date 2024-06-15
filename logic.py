import sqlite3
from datetime import datetime, timedelta


class TaskLogic:
    def __init__(self):
        self.conn = sqlite3.connect("tasks.db")
        self.cursor = self.conn.cursor()
        self.conn.commit()

    def save_task(self, name, task_type, duration):
        self.cursor.execute(
            """
            INSERT INTO tasks (date, name, type, duration) VALUES (?, ?, ?, ?)
        """,
            (
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                name,
                task_type,
                duration,
            ),
        )
        self.conn.commit()

    def view_tasks(self):
        today = datetime.now().strftime("%Y-%m-%d")
        week = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        month = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")

        self.cursor.execute(
            "SELECT type, SUM(duration) FROM tasks WHERE date >= ? GROUP BY type",
            (today,),
        )
        result_day = self.cursor.fetchall()

        self.cursor.execute(
            "SELECT type, SUM(duration) FROM tasks WHERE date >= ? GROUP BY type",
            (week,),
        )
        result_week = self.cursor.fetchall()

        self.cursor.execute(
            "SELECT type, SUM(duration) FROM tasks WHERE date >= ? GROUP BY type",
            (month,),
        )
        result_month = self.cursor.fetchall()

        return result_day, result_week, result_month

    def get_task_types(self):
        self.cursor.execute("SELECT name FROM types")
        return self.cursor.fetchall()
