from fastapi import FastAPI
import sqlite3
from ingredient import Ingredient
from lookup import lookup

app = FastAPI()

def get_db_connection():
    conn = sqlite3.connect("../SQL/gastronomic.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/")
async def root():
    conn = get_db_connection()
    cursor = conn.cursor()
    users = cursor.execute("SELECT * FROM users")
    conn.close()
    return users

@app.post("/ingredients/")
async def create_ingredient(ingredient: Ingredient):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO ingredients (user_id, name, servings, amount, calories, protein, fat, carbs)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        ingredient.user_id,
        ingredient.name,
        ingredient.servings,
        ingredient.amount,
        ingredient.calories,
        ingredient.protein,
        ingredient.fat,
        ingredient.carbs
    ))

    conn.commit()
    conn.close()

    return {"message": "Ingredient added successfully", "ingredient": ingredient}