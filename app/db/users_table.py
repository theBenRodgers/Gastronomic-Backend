from typing import List
from app.db.connect import get_db_connection
from app.schemas.models.user import User

def create_user(uid: str, user: User):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (user_id, fname, lname, intolerances, diets)
        VALUES (?, ?, ?, ?);
    """, (
        uid,
        user.fname,
        user.lname,
        user.intolerances,
        user.diets,
    ))

    conn.commit()
    cursor.close()
    conn.close()

def select_user(uid: str) -> User:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM users
        WHERE user_id = ?;
    """, (uid,))

    row = cursor.fetchone()[0]
    conn.close()

    return User(
        fname=row["fname"],
        lname=row["lname"],
        intolerances=row["intolerances"].split(
            ",") if row["intolerances"] else None,
        diets=row["diets"].split(
            ",") if row["diets"] else None
    )


def update_user(uid: str, user: User):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE user
        SET fname = ?, lnane = ?, intolerances = ?, diets = ?
        WHERE user_id = ?;
    """, (
        user.fname,
        user.lname,
        ",".join(user.intolerances) if user.intolerances else None,
        ",".join(user.diets) if user.diets else None,
        uid
    ))

    conn.commit()
    cursor.close()
    conn.close()

def delete_user(uid: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM users
        WHERE user_id = ?;
    """, (uid))

    conn.commit()
    conn.close()