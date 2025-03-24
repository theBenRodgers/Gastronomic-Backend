CREATE TABLE ingredients (
    ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id TEXT NOT NULL,
    name TEXT,
    brand TEXT,
    servings INTEGER NOT NULL,
    amount INTEGER NOT NULL,
    calories INTEGER,
    protein INTEGER,
    fat INTEGER,
    carbs INTEGER
);
