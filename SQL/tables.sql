CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    fName TEXT NOT NULL, 
    lName TEXT NOT NULL, 
    email TEXT NOT NULL, 
    dob TEXT NOT NULL
);

CREATE TABLE ingredients (
    ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    name TEXT,
    servings INTEGER,
    amount INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);

CREATE TABLE nutrition (
    ingredient_id INTEGER PRIMARY KEY NOT NULL,
    calories INTEGER,
    protein INTEGER,
    fat INTEGER,
    carbs INTEGER,
    sugar INTEGER,
    fiber INTEGER,
    sodium INTEGER,
    cholesterol INTEGER,
    FOREIGN KEY (ingredient_id) REFERENCES ingredients (ingredient_id) UNIQUE
);
