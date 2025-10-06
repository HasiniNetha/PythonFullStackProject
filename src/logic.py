from src.db import get_all_drinks

def recommend_by_flavor(base_flavor: str, drink_type: str = None):
    """Return drinks matching a given flavor and (optional) type"""
    drinks = get_all_drinks()
    if not drinks:
        return ["⚠️ No drinks found in database! Please insert sample data."]

    results = []
    for d in drinks:
        if base_flavor.capitalize() in d["flavors"]:
            if not drink_type or d["type"].lower() == drink_type.lower():
                results.append(d["name"])

    # Remove duplicates and sort alphabetically
    unique_results = sorted(list(set(results)))

    return unique_results if unique_results else ["❌ No matching drinks found! Try another flavor."]
