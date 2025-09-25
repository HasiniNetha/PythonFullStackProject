from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.logic import DiaryManager
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



# ----- App Setup -----
app = FastAPI(title="Micro Diary API", version="1.0")

# ----- Allow Frontend (Streamlit/React) to call the API -----
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (frontend apps)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create an instance of DiaryManager
diary_manager = DiaryManager()

# ============================
# Pydantic Models (Schemas)
# ============================

class UserCreate(BaseModel):
    username: str
    email: str
    password_hash: str

class EntryCreate(BaseModel):
    user_id: int
    content: str
    mood: str | None = None
    tags: list[str] | None = []

class EntryUpdate(BaseModel):
    content: str | None = None
    mood: str | None = None
    tags: list[str] | None = None


# ============================
# Root Endpoint
# ============================
@app.get("/")
def home():
    """Check if the API is running."""
    return {"message": "Micro Diary API is running!"}


# ============================
# User Endpoints
# ============================

@app.post("/users")
def create_user(user: UserCreate):
    """Register a new user."""
    result = diary_manager.add_user(user.username, user.email, user.password_hash)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result


@app.get("/users")
def get_all_users():
    """Get all registered users."""
    return diary_manager.get_all_users()


@app.get("/users/{user_id}")
def get_user(user_id: int):
    """Get a single user by ID."""
    result = diary_manager.get_user_by_id(user_id)
    if not result.get("Success"):
        raise HTTPException(status_code=404, detail=result.get("message"))
    return result


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    """Delete a user by ID."""
    result = diary_manager.delete_user(user_id)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result


# ============================
# Entry Endpoints
# ============================

@app.post("/entries")
def create_entry(entry: EntryCreate):
    """Create a new journal entry."""
    result = diary_manager.add_entry(
        entry.user_id,
        entry.content,
        mood=entry.mood,
        tags=entry.tags
    )
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result


@app.get("/entries")
def get_entries(limit: int = 50, offset: int = 0):
    """Get all journal entries with pagination."""
    return diary_manager.get_entries(limit, offset)


@app.get("/entries/user/{user_id}")
def get_entries_by_user(user_id: int, limit: int = 50, offset: int = 0):
    """Get all entries for a specific user."""
    return diary_manager.get_entries_by_user(user_id, limit, offset)


@app.put("/entries/{entry_id}")
def update_entry(entry_id: int, entry: EntryUpdate):
    """Update a journal entry."""
    result = diary_manager.update_entry(
        entry_id,
        content=entry.content,
        mood=entry.mood,
        tags=entry.tags
    )
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result


@app.delete("/entries/{entry_id}")
def delete_entry(entry_id: int):
    """Delete a journal entry."""
    result = diary_manager.delete_entry(entry_id)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result


# ============================
# Search and Filter Endpoints
# ============================

@app.get("/entries/search")
def search_entries(query: str, limit: int = 50, offset: int = 0):
    """Search entries using full-text search."""
    result = diary_manager.search_entries(query, limit, offset)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result


@app.get("/entries/filter/mood/{mood}")
def filter_entries_by_mood(mood: str, limit: int = 50, offset: int = 0):
    """Filter entries by mood."""
    return diary_manager.filter_entries_by_mood(mood, limit, offset)


@app.get("/entries/filter/tag/{tag}")
def filter_entries_by_tag(tag: str, limit: int = 50, offset: int = 0):
    """Filter entries by tag."""
    return diary_manager.filter_entries_by_tag(tag, limit, offset)


# ============================
# Mood Statistics
# ============================

@app.get("/entries/stats/{user_id}")
def get_mood_statistics(user_id: int):
    """Get mood statistics for a user."""
    result = diary_manager.get_mood_stats(user_id)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result
