import pandas as pd
import time
from playwright.sync_api import sync_playwright

def scrape_130point(search_query):
    with sync_playwright() as p:
        # Launch browser (headless=False lets you watch it work)
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()
        
        print(f"Navigating to 130point for: {search_query}")
        page.goto("https://130point.com/sales/", wait_until="domcontentloaded", timeout=60000)
        
        # 1. Handle the Search Bar
        search_input = page.locator("#searchBar")
        search_input.wait_for(state="visible", timeout=60000)
        search_input.fill(search_query)
        page.keyboard.press("Enter")
        
        # 2. Wait for the results table to generate rows
        print("Waiting for table to populate...")
        # 130point uses #dRow for the individual result rows
        page.wait_for_selector("#dRow", timeout=20000)
        
        # 3. Scrape the data
        rows = page.locator("#dRow").all()
        card_data = []

        for row in rows:
            try:
                # Use the 'data-price' attribute for the TRUE best offer price
                true_price = row.get_attribute("data-price")
                title = row.locator("#titleText a").inner_text()
                date_text = row.locator("#dateText").inner_text()
                
                card_data.append({
                    "Title": title.strip(),
                    "True_Price_USD": float(true_price) if true_price else 0.0,
                    "Date": date_text.replace("Date: ", "").strip()
                })
            except Exception as e:
                # Skip rows that don't match the format
                continue

        browser.close()
        
        # 4. Save to CSV
        if card_data:
            df = pd.DataFrame(card_data)
            print("Success! Scraped Data:")
            print(df.head())
            df.to_csv("true_market_prices.csv", index=False)
            print(f"Saved {len(df)} sales to true_market_prices.csv")
        else:
            print("No data found. Try a different search query.")

if __name__ == "__main__":
    # Your target card
    scrape_130point("2025-26 Pokemon Scarlet & Violet #SV001 Charizard VMAX")