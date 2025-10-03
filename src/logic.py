from src.db import get_all_drinks

def recommend_by_flavor(base_flavor: str, drink_type: str = None):
    """Return drinks that match a given flavor and optional type"""
    drinks = get_all_drinks()
    results = []

    for d in drinks:
        if base_flavor.capitalize() in d["flavors"]:
            if drink_type is None or d["type"].lower() == drink_type.lower():
                results.append(d["name"])

    return results if results else ["No matching drinks found!"]
