from src.db import (
    create_user, get_all_users, get_user_by_id,
    update_user, delete_user,
    create_entry, get_all_entries, get_entries_by_user,
    filter_entries_by_mood, filter_entries_by_tag,
    update_entry, delete_entry,
    search_entries, get_mood_statistics
)


class DiaryManager:
    """
    Business logic for Micro Diary API.
    Bridges frontend/API and database operations.
    """

    # ============================
    # USER LOGIC
    # ============================

    def add_user(self, username: str, email: str, password_hash: str):
        if not all([username, email, password_hash]):
            return {"Success": False, "message": "Username, email, and password are required."}

        response = create_user(username, email, password_hash)
        if response.error is None:
            return {"Success": True, "message": "User created successfully.", "data": response.data}
        return {"Success": False, "message": f"Failed to create user: {response.error}"}

    def get_users(self):
        response = get_all_users()
        if response.error is None:
            if response.data:
                return {"Success": True, "data": response.data}
            return {"Success": False, "message": "No users found."}
        return {"Success": False, "message": f"Failed to fetch users: {response.error}"}

    def get_user(self, user_id: int):
        if not user_id:
            return {"Success": False, "message": "User ID is required."}

        response = get_user_by_id(user_id)
        if response.error is None:
            if response.data:
                return {"Success": True, "data": response.data}
            return {"Success": False, "message": "User not found."}
        return {"Success": False, "message": f"Failed to fetch user: {response.error}"}

    def update_user(self, user_id: int, username=None, email=None, password_hash=None):
        if not user_id:
            return {"Success": False, "message": "User ID is required for update."}
        if not any([username, email, password_hash]):
            return {"Success": False, "message": "At least one field must be provided to update."}

        response = update_user(user_id, username, email, password_hash)
        if response.error is None:
            return {"Success": True, "message": "User updated successfully.", "data": response.data}
        return {"Success": False, "message": f"Failed to update user: {response.error}"}

    def delete_user(self, user_id: int):
        if not user_id:
            return {"Success": False, "message": "User ID is required for deletion."}

        response = delete_user(user_id)
        if response.error is None:
            return {"Success": True, "message": "User deleted successfully."}
        return {"Success": False, "message": f"Failed to delete user: {response.error}"}

    # ============================
    # JOURNAL ENTRY LOGIC
    # ============================

    def add_entry(self, user_id: int, content: str, mood=None, tags=None):
        if not user_id or not content:
            return {"Success": False, "message": "User ID and content are required to create an entry."}

        tags = tags or []
        response = create_entry(user_id, content, mood, tags)
        if response.error is None:
            return {"Success": True, "message": "Entry created successfully.", "data": response.data}
        return {"Success": False, "message": f"Failed to create entry: {response.error}"}

    def get_entries(self, limit=50, offset=0):
        response = get_all_entries(limit, offset)
        if response.error is None:
            if response.data:
                return {"Success": True, "data": response.data}
            return {"Success": False, "message": "No entries found."}
        return {"Success": False, "message": f"Failed to fetch entries: {response.error}"}

    def get_entries_by_user(self, user_id: int, limit=50, offset=0):
        if not user_id:
            return {"Success": False, "message": "User ID is required."}

        response = get_entries_by_user(user_id, limit, offset)
        if response.error is None:
            if response.data:
                return {"Success": True, "data": response.data}
            return {"Success": False, "message": "No entries found for this user."}
        return {"Success": False, "message": f"Failed to fetch entries: {response.error}"}

    def filter_entries_by_mood(self, mood: str, limit=50, offset=0):
        if not mood:
            return {"Success": False, "message": "Mood filter is required."}

        response = filter_entries_by_mood(mood, limit, offset)
        if response.error is None:
            if response.data:
                return {"Success": True, "data": response.data}
            return {"Success": False, "message": f"No entries found for mood '{mood}'."}
        return {"Success": False, "message": f"Failed to fetch entries: {response.error}"}

    def filter_entries_by_tag(self, tag: str, limit=50, offset=0):
        if not tag:
            return {"Success": False, "message": "Tag filter is required."}

        response = filter_entries_by_tag(tag, limit, offset)
        if response.error is None:
            if response.data:
                return {"Success": True, "data": response.data}
            return {"Success": False, "message": f"No entries found with tag '{tag}'."}
        return {"Success": False, "message": f"Failed to fetch entries: {response.error}"}

    def update_entry(self, entry_id: int, content=None, mood=None, tags=None):
        if not entry_id:
            return {"Success": False, "message": "Entry ID is required for update."}
        if not any([content, mood, tags]):
            return {"Success": False, "message": "At least one field must be provided to update."}

        response = update_entry(entry_id, content, mood, tags)
        if response.error is None:
            return {"Success": True, "message": "Entry updated successfully.", "data": response.data}
        return {"Success": False, "message": f"Failed to update entry: {response.error}"}

    def delete_entry(self, entry_id: int):
        if not entry_id:
            return {"Success": False, "message": "Entry ID is required for deletion."}

        response = delete_entry(entry_id)
        if response.error is None:
            return {"Success": True, "message": "Entry deleted successfully."}
        return {"Success": False, "message": f"Failed to delete entry: {response.error}"}

    # ============================
    # SEARCH & ANALYTICS
    # ============================

    def search_entries(self, query: str, limit=50, offset=0):
        if not query:
            return {"Success": False, "message": "Search query cannot be empty."}

        response = search_entries(query, limit, offset)
        if response.error is None:
            if response.data:
                return {"Success": True, "data": response.data}
            return {"Success": False, "message": "No entries found matching your search."}
        return {"Success": False, "message": f"Failed to perform search: {response.error}"}

    def get_mood_statistics(self, user_id: int):
        if not user_id:
            return {"Success": False, "message": "User ID is required to get mood statistics."}

        response = get_mood_statistics(user_id)
        if response.error is None:
            return {"Success": True, "data": response.data}
        return {"Success": False, "message": f"Failed to get mood statistics: {response.error}"}
