import pandas as pd

collection = pd.read_excel("C:\\Users\\ddrom\\OneDrive\\Documents\\Card Collection 2.0\\My_Collection.xlsx")

collection_cleaned = collection[["Year", "Brand", "Set", "Card_Number", "Player", "Team", "Parallel", "Quantity"]]

collection_cleaned["Parallel"] = collection_cleaned["Parallel"].str.replace("Base Set -", "", regex=False).str.strip()
collection_cleaned["Parallel"] = collection_cleaned["Parallel"].str.replace("Parallel", "", regex=False).str.strip()
collection_cleaned["Parallel"] = collection_cleaned["Parallel"].str.replace("'s", "", regex=False).str.strip()
collection_cleaned["Parallel"] = collection_cleaned["Parallel"].str.replace(" - ", "", regex=False).str.strip()
collection_cleaned["Parallel"] = collection_cleaned["Parallel"].replace("Base Set", "")
collection_cleaned["Parallel"] = collection_cleaned["Parallel"].replace("Base", "")

collection_cleaned["Price_USD"] = 0.0

collection_cleaned.to_csv("data\\cleaned_collection.csv", index=False) 
