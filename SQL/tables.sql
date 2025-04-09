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

-- Recipes Table
CREATE TABLE IF NOT EXISTS recipes (
    recipe_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id TEXT NOT NULL,           
    title TEXT NOT NULL,            
    instructions TEXT NOT NULL,      
    prep_time INTEGER,               
    cook_time INTEGER,               
    servings INTEGER,                
    calories INTEGER,                
    protein INTEGER,                
    fat INTEGER,                     
    carbs INTEGER,                   
    source_url TEXT,                 
);

-- Recipe-Ingredients Relationship Table
CREATE TABLE IF NOT EXISTS recipe_ingredients (
    recipe_id INTEGER NOT NULL,          
    ingredient_id INTEGER NOT NULL,     
    quantity INTEGER NOT NULL,        
    PRIMARY KEY (recipe_id, ingredient_id),
    FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id)
);