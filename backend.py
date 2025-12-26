from mock_db import create_order, get_order

def get_menu():
    return [
        {"name": "Margherita", "sizes": ["Small", "Medium", "Large"]},
        {"name": "Pepperoni", "sizes": ["Medium", "Large"]},
        {"name": "Veg Supreme", "sizes": ["Medium", "Large"]},
        {"name": "Chicken BBQ", "sizes": ["Medium", "Large"]},
    ]

def place_order(pizza, size):
    return create_order(pizza, size)

def track_order(order_id):
    return get_order(order_id)

MCP_TOOLS = {
    "get_menu": get_menu,
    "place_order": place_order,
    "track_order": track_order
}
