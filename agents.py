from groq_client import GroqLLM
from mock_db import update_order

AVAILABLE_PIZZAS = [
    "margherita",
    "pepperoni",
    "veg supreme",
    "chicken bbq",
    "farmhouse",
    "paneer tikka"
]

AVAILABLE_SIZES = ["small", "medium", "large"]
AVAILABLE_ADDONS = ["extra cheese", "olives", "jalapenos", "mushrooms", "coke"]


class OrderingAgent:
    def __init__(self, tools):
        self.tools = tools
        self.llm = GroqLLM()
        self.current_order_id = None

    def handle(self, user_text):
        text = user_text.lower()

        # ---------- ALWAYS PARSE FULL INTENT ----------
        prompt = f"""
User wants to order or modify a pizza.

Sentence:
"{user_text}"

Extract:
- pizza name
- size
- addon (if any)

Rules:
- If pizza is missing, keep existing pizza or assume margherita
- If size is missing, keep existing size or assume medium
- Reply in one line like:
pizza=farmhouse, size=large, addon=extra cheese
"""

        response = self.llm.ask(prompt)

        # -------- DEFAULTS --------
        pizza = None
        size = None
        addon = None

        for p in AVAILABLE_PIZZAS:
            if p in response:
                pizza = p.title()
                break

        for s in AVAILABLE_SIZES:
            if s in response:
                size = s.title()
                break

        for a in AVAILABLE_ADDONS:
            if a in response:
                addon = a.title()
                break

        # ---------- IF ORDER EXISTS → UPDATE ----------
        if self.current_order_id:
            updated = update_order(
                self.current_order_id,
                pizza=pizza,
                size=size,
                addon=addon
            )
            return {
                "order_id": self.current_order_id,
                "details": updated
            }

        # ---------- ELSE → CREATE NEW ORDER ----------
        if not pizza:
            pizza = "Margherita"
        if not size:
            size = "Medium"

        order_id, details = self.tools["place_order"](
            pizza=pizza,
            size=size
        )

        # add addon once (if present)
        if addon:
            update_order(order_id, addon=addon)

        self.current_order_id = order_id

        return {
            "order_id": order_id,
            "details": details
        }


class SchedulingAgent:
    def receive(self, order_info):
        print(f"📦 Order {order_info['order_id']} updated")
