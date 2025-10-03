import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SUPABASE_URL="https://gcnlzbzmsxrworthtjxn.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imdjbmx6Ynptc3hyd29ydGh0anhuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODI1ODYsImV4cCI6MjA3MzY1ODU4Nn0.IKZOBmQo22TCSFHHnrzgGiGczu9kx04gmHc9fSPcoqM"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def insert_sample_data():
    """Insert comprehensive sample drinks into the database"""
    sample_drinks = [
        # 🍫 Chocolate
        {"name": "Oreo Shake", "type": "Shake", "flavors": ["Chocolate", "Sweet", "Creamy"]},
        {"name": "Choco Chip Shake", "type": "Shake", "flavors": ["Chocolate", "Sweet"]},
        {"name": "Choco Burst Juice", "type": "Juice", "flavors": ["Chocolate", "Sweet"]},
        {"name": "Dark Cocoa Juice", "type": "Juice", "flavors": ["Chocolate", "Tangy"]},
        {"name": "Hot Chocolate", "type": "Drink", "flavors": ["Chocolate", "Sweet", "Warm"]},
        {"name": "Iced Mocha", "type": "Drink", "flavors": ["Chocolate", "Creamy"]},

        # 🥭 Mango
        {"name": "Mango Shake", "type": "Shake", "flavors": ["Mango", "Sweet", "Creamy"]},
        {"name": "Mango Delight Shake", "type": "Shake", "flavors": ["Mango", "Fruity"]},
        {"name": "Mango Juice", "type": "Juice", "flavors": ["Mango", "Sweet"]},
        {"name": "Tropical Mango Juice", "type": "Juice", "flavors": ["Mango", "Tangy", "Fruity"]},
        {"name": "Mango Cooler", "type": "Drink", "flavors": ["Mango", "Cool", "Sweet"]},
        {"name": "Spicy Mango Drink", "type": "Drink", "flavors": ["Mango", "Tangy", "Spicy"]},

        # 🍓 Strawberry
        {"name": "Strawberry Shake", "type": "Shake", "flavors": ["Strawberry", "Sweet", "Fruity"]},
        {"name": "Berry Blast Shake", "type": "Shake", "flavors": ["Strawberry", "Creamy"]},
        {"name": "Strawberry Juice", "type": "Juice", "flavors": ["Strawberry", "Fruity"]},
        {"name": "Tangy Strawberry Juice", "type": "Juice", "flavors": ["Strawberry", "Tangy", "Sweet"]},
        {"name": "Strawberry Iced Tea", "type": "Drink", "flavors": ["Strawberry", "Cool", "Fruity"]},
        {"name": "Strawberry Soda", "type": "Drink", "flavors": ["Strawberry", "Sweet", "Fizz"]},

        # 🍍 Pineapple
        {"name": "Pineapple Shake", "type": "Shake", "flavors": ["Pineapple", "Sweet", "Creamy"]},
        {"name": "Tropical Pineapple Shake", "type": "Shake", "flavors": ["Pineapple", "Fruity"]},
        {"name": "Pineapple Juice", "type": "Juice", "flavors": ["Pineapple", "Tangy", "Sweet"]},
        {"name": "Zesty Pineapple Juice", "type": "Juice", "flavors": ["Pineapple", "Tangy", "Fruity"]},
        {"name": "Pineapple Fizz", "type": "Drink", "flavors": ["Pineapple", "Fizz", "Cool"]},
        {"name": "Spiced Pineapple Drink", "type": "Drink", "flavors": ["Pineapple", "Spicy", "Sweet"]},

        # 🌰 Nutty
        {"name": "Ferrero Rocher Shake", "type": "Shake", "flavors": ["Chocolate", "Nutty", "Sweet"]},
        {"name": "Nutty Vanilla Shake", "type": "Shake", "flavors": ["Nutty", "Creamy", "Sweet"]},
        {"name": "Nut Punch Juice", "type": "Juice", "flavors": ["Nutty", "Sweet"]},
        {"name": "Almond Delight Juice", "type": "Juice", "flavors": ["Nutty", "Creamy"]},
        {"name": "Cashew Milk Drink", "type": "Drink", "flavors": ["Nutty", "Sweet", "Warm"]},
        {"name": "Hazelnut Cold Brew", "type": "Drink", "flavors": ["Nutty", "Cool", "Bitter"]},

        # 🍬 Sweet (already covered in most)
        {"name": "Sweet Banana Shake", "type": "Shake", "flavors": ["Sweet", "Creamy"]},
        {"name": "Sweet Lassi", "type": "Juice", "flavors": ["Sweet", "Creamy"]},
        {"name": "Rose Milk Drink", "type": "Drink", "flavors": ["Sweet", "Floral"]},

        # 🧊 Cool
        {"name": "Minty Shake", "type": "Shake", "flavors": ["Cool", "Creamy"]},
        {"name": "Lime Cooler Juice", "type": "Juice", "flavors": ["Cool", "Tangy"]},
        {"name": "Iced Lemon Drink", "type": "Drink", "flavors": ["Cool", "Citrus"]},
    ]

    for drink in sample_drinks:
        supabase.table("drinks").insert(drink).execute()

    return "✅ Sample data inserted!"


def get_all_drinks():
    """Fetch all drinks from database"""
    return supabase.table("drinks").select("*").execute().data
