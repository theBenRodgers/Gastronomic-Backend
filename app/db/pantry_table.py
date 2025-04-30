from typing import List
from app.db.connect import get_db_connection
from app.schemas.models.pantry_item import PantryItem


def select_pantry(uid: str) -> List[PantryItem]:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            *
        FROM pantry
        WHERE user_id = ?
    """, (uid,))

    rows = cursor.fetchall()
    conn.close()

    pantry_items = []
    for row in rows:
        pantry_item = PantryItem(
            pantry_id=row["pantry_id"],
            kind=row["kind"],
            id=row["id"],
            name=row["name"],
            image=row["image"],
            brand=row["brand"],
            imageType=row["imageType"],
            unit=row["unit"],
            possibleUnits=row["possibleUnits"].split(
                ",") if row["possibleUnits"] else None,
            estimatedCost=row["estimatedCost"],
            shoppingListUnits=row["shoppingListUnits"].split(
                ",") if row["shoppingListUnits"] else None,
            aisle=row["aisle"],
            categoryPath=row["categoryPath"].split(
                ",") if row["categoryPath"] else None,
            weightPerServing=float(
                row["weightPerServing"]) if row["weightPerServing"] else None,
            upc=row["upc"],
            price=row["price"],
            calories=row["calories"],
            fat=row["fat"],
            protein=row["protein"],
            carbs=row["carbs"],
            amount=row["amount"],
            expirationDate=row["expirationDate"]
        )
        pantry_items.append(pantry_item)

    return pantry_items


def count_pantry(uid) -> int:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*) FROM pantry
        WHERE user_id = ?;
    """, (uid,))

    count = cursor.fetchone()[0]
    conn.close()

    return count


def select_pantry_item(uid: str, pantry_id: int) -> PantryItem:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM pantry
        WHERE user_id = ? AND pantry_id = ?;
    """, (uid, pantry_id))

    row = cursor.fetchone()[0]
    conn.close()

    return PantryItem(
        pantry_id=row["pantry_id"],
        kind=row["kind"],
        id=row["id"],
        name=row["name"],
        image=row["image"],
        brand=row["brand"],
        imageType=row["imageType"],
        unit=row["unit"],
        possibleUnits=row["possibleUnits"].split(
            ",") if row["possibleUnits"] else None,
        estimatedCost=row["estimatedCost"],
        shoppingListUnits=row["shoppingListUnits"].split(
            ",") if row["shoppingListUnits"] else None,
        aisle=row["aisle"],
        categoryPath=row["categoryPath"].split(
            ",") if row["categoryPath"] else None,
        weightPerServing=float(
            row["weightPerServing"]) if row["weightPerServing"] else None,
        upc=row["upc"],
        price=row["price"],
        calories=row["calories"],
        fat=row["fat"],
        protein=row["protein"],
        carbs=row["carbs"],
        amount=row["amount"],
        expirationDate=row["expirationDate"]
    )


def create_pantry_item(uid: str, item: PantryItem):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO pantry (
            kind, id, name, image, brand, imageType,
            unit, possibleUnits, estimatedCost, shoppingListUnits,
            aisle, categoryPath, weightPerServing,
            upc, price,
            calories, fat, protein, carbs, amount, expirationDate,
            user_id
        )
        VALUES (
            ?, ?, ?, ?, ?, ?, 
            ?, ?, ?, ?, 
            ?, ?, ?, 
            ?, ?, 
            ?, ?, ?, ?, ?, ?, 
            ?
        );
    """, (
        item.kind,
        item.id,
        item.name,
        item.image,
        item.brand,
        item.imageType,
        item.unit,
        ",".join(item.possibleUnits) if item.possibleUnits else None,
        item.estimatedCost,
        ",".join(item.shoppingListUnits) if item.shoppingListUnits else None,
        item.aisle,
        ",".join(item.categoryPath) if item.categoryPath else None,
        item.weightPerServing,
        item.upc,
        item.price,
        item.calories,
        item.fat,
        item.protein,
        item.carbs,
        item.amount,
        item.expirationDate,
        uid  # this is the user's ID
    ))

    conn.commit()
    conn.close()


def update_pantry_item(uid: str, item: PantryItem):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE pantry
        SET
            kind = ?, id = ?, name = ?, image = ?, brand = ?, imageType = ?,
            unit = ?, possibleUnits = ?, estimatedCost = ?, shoppingListUnits = ?,
            aisle = ?, categoryPath = ?, weightPerServing = ?,
            upc = ?, price = ?,
            calories = ?, fat = ?, protein = ?, carbs = ?, amount = ?, expirationDate = ?
        WHERE pantry_id = ? AND user_id = ?;
    """, (
        item.kind,
        item.id,
        item.name,
        item.image,
        item.brand,
        item.imageType,
        item.unit,
        ",".join(item.possibleUnits) if item.possibleUnits else None,
        item.estimatedCost,
        ",".join(item.shoppingListUnits) if item.shoppingListUnits else None,
        item.aisle,
        ",".join(item.categoryPath) if item.categoryPath else None,
        item.weightPerServing,
        item.upc,
        item.price,
        item.calories,
        item.fat,
        item.protein,
        item.carbs,
        item.amount,
        item.expirationDate,
        item.pantry_id,
        uid
    ))

    conn.commit()
    conn.close()


def delete_pantry_item(uid: str, pantry_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM pantry
        WHERE pantry_id = ? AND user_id = ?;
    """, (pantry_id, uid))

    conn.commit()
    conn.close()
