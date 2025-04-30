import sqlite3

def get_db_connection():
    conn = sqlite3.connect(r"C:\Gastronomic-Backend\sql\gastronomic.db")
    conn.row_factory = sqlite3.Row
    return conn

def reset():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE * from ingredients
        WHERE user_id = ?;
    """,(uid,))

    cursor.execute("""
        DELETE * from recipes
        WHERE user_id = ?;
    """,(uid,))

    cursor.execute("""
        DELETE * from users
        WHERE user_id = ?;
    """,(uid,))

    conn.commit()
    cursor.close()
    conn.close()