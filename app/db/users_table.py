import sqlite3
from typing import List, Optional
from app.db.connect import get_db_connection
from app.schemas.models.user import User

def insert_user(uid: str, user: User) -> None:
    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (user_id, fname, lname, intolerances, diets)
        VALUES (?, ?, ?, ?, ?);
    """, (
        uid,
        user.fname,
        user.lname,
        ",".join(user.intolerances) if user.intolerances else "",
        ",".join(user.diets) if user.diets else "",
    ))

    conn.commit()
    cursor.close()
    conn.close()

def select_user(uid: str) -> Optional[User]:
    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT user_id, fname, lname, intolerances, diets
        FROM users
        WHERE user_id = ?;
    """, (uid,))

    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row is None:
        return None

    return User(
        fname=row["fname"],
        lname=row["lname"],
        intolerances=row["intolerances"].split(",") if row["intolerances"] else [],
        diets=row["diets"].split(",") if row["diets"] else []
    )

def update_user(uid: str, user: User) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET fname = ?, lname = ?, intolerances = ?, diets = ?
        WHERE user_id = ?;
    """, (
        user.fname,
        user.lname,
        ",".join(user.intolerances) if user.intolerances else "",
        ",".join(user.diets) if user.diets else "",
        uid
    ))

    conn.commit()
    cursor.close()
    conn.close()

def delete_user(uid: str) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM users
        WHERE user_id = ?;
    """, (uid,))

    conn.commit()
    cursor.close()
    conn.close()
