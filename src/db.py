import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load .env credentials
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Create Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def check_connection():
    """Check if Supabase is reachable"""
    try:
        response = supabase.table("drinks").select("*").limit(1).execute()
        return "✅ Connected to Supabase"
    except Exception as e:
        return f"❌ Connection failed: {e}"


def insert_sample_data():
    """Insert some sample drinks"""
    sample_drinks = [
        {"name": "Oreo Shake", "type": "Shake", "flavors": ["Chocolate", "Sweet", "Creamy"]},
        {"name": "Choco Chip Shake", "type": "Shake", "flavors": ["Chocolate", "Sweet"]},
        {"name": "Ferrero Rocher Thickshake", "type": "Shake", "flavors": ["Chocolate", "Nutty", "Sweet"]},
        {"name": "Mango Shake", "type": "Shake", "flavors": ["Mango", "Sweet", "Creamy"]},
        {"name": "Strawberry Shake", "type": "Shake", "flavors": ["Strawberry", "Sweet", "Fruity"]},
        {"name": "Hot Chocolate", "type": "Drink", "flavors": ["Chocolate", "Sweet", "Warm"]},
        {"name": "Pineapple Juice", "type": "Juice", "flavors": ["Pineapple", "Tangy", "Sweet"]}
    ]

    try:
        for drink in sample_drinks:
            supabase.table("drinks").insert(drink).execute()
        return "✅ Sample data inserted successfully!"
    except Exception as e:
        return f"❌ Failed to insert data: {e}"


def get_all_drinks():
    """Fetch all drinks from the database"""
    try:
        data = supabase.table("drinks").select("*").execute()
        return data.data
    except Exception as e:
        print("Database fetch error:", e)
        return []
