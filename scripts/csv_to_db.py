import sqlite3

db = sqlite3.connect("value_history.db")
csv = "hockey-card-tracker\hockey-card-tracker\data\cleaned_collection.csv"

cursor = db.cursor()

with open(csv, "r", encoding="utf-8") as f:
    # Skip header line
    next(f)
    
    for line in f:
        parts = line.strip().split(",")
        if len(parts) < 8:
            continue  # Skip malformed lines
        
        
        year = parts[0].strip()
        brand = parts[1].strip()
        set_name = parts[2].strip()
        card_number = parts[3].strip()
        player_name = parts[4].strip()
        team = parts[5].strip()
        parallel = parts[6].strip()

        card_id = f"{year}_{brand}_{set_name}_{card_number}_{player_name}_{parallel or 'base'}".replace(" ", "_").lower()

        print(card_id)
