import uuid

ORDERS = {}

def create_order(pizza, size):
    order_id = str(uuid.uuid4())[:8]
    ORDERS[order_id] = {
        "pizza": pizza,
        "size": size,
        "addons": [],
        "status": "Preparing",
        "eta": "30 minutes"
    }
    return order_id, ORDERS[order_id]

def update_order(order_id, pizza=None, size=None, addon=None):
    order = ORDERS.get(order_id)
    if not order:
        return None

    if pizza:
        order["pizza"] = pizza

    if size:
        order["size"] = size

    if addon and addon not in order["addons"]:
        order["addons"].append(addon)

    return order


def get_order(order_id):
    return ORDERS.get(order_id)
