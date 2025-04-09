import sqlite3
from app.schemas.ingredient import Ingredient

def get_db_connection():
    conn = sqlite3.connect(r"C:\Gastronomic-Backend\sql\gastronomic.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def insert_ingredient(uid : str, ingredient : Ingredient):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO ingredients (user_id, name, brand, servings, amount, calories, protein, fat, carbs)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, (
        uid,
        ingredient.name,
        ingredient.brand,
        ingredient.servings,
        ingredient.amount,
        ingredient.calories,
        ingredient.protein,
        ingredient.fat,
        ingredient.carbs
    ))

    conn.commit()
    cursor.close()
    conn.close()

def select_ingredients(uid : str):
    conn = get_db_connection()
    cursor = conn.cursor()

    ingredients = cursor.execute("""
        SELECT * FROM ingredients 
        WHERE user_id = ?;
    """,(uid,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    return results

def update_ingredient(uid : str, iid : int, ingredient : Ingredient):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE ingredients
        SET name = ?, brand = ?, servings = ?, amount = ? , calories = ?, protein = ?, fat = ?, carbs = ?
        WHERE ingredient_id = ?
        AND user_id = ?;
    """, (
        ingredient.name,
        ingredient.servings,
        ingredient.brand,
        ingredient.amount,
        ingredient.calories,
        ingredient.protein,
        ingredient.fat,
        ingredient.carbs,
        iid,
        uid
    ))

    conn.commit()
    cursor.close()
    conn.close()

def delete_ingredient(uid : str, iid : int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM ingredients
        WHERE ingredient_id = ?
        AND user_id = ?;
    """, (
        iid,
        uid
    ))

    conn.commit()
    cursor.close()
    conn.close()