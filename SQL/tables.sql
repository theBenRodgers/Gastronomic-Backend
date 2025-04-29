CREATE TABLE users (
    user_id TEXT PRIMARY KEY NOT NULL,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    intolerances TEXT,
    diets TEXT
)

CREATE TABLE pantry (
    pantry_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    kind TEXT NOT NULL,
    id INTEGER NOT NULL,

    name TEXT,
    image TEXT,
    brand TEXT,
    imageType TEXT,

    unit TEXT,
    possibleUnits TEXT,
    estimatedCost FLOAT,
    shoppingListUnits TEXT,
    aisle TEXT,
    categoryPath TEXT,
    weightPerServing TEXT,

    upc TEXT,
    price FLOAT,


    calories INTEGER,
    fat INTEGER,
    protein INTEGER,
    carbs INTEGER,
    amount INTEGER,
    expirationDate TEXT,

    user_id TEXT NOT NULL
);

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