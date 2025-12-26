import streamlit as st
from backend import MCP_TOOLS
from agents import OrderingAgent, SchedulingAgent

st.set_page_config(page_title="Mission Pizza 🍕", layout="centered")

st.title("🍕 Mission Pizza")
st.write("AI-powered pizza ordering using Groq + MCP-style agents")

if "ordering_agent" not in st.session_state:
    st.session_state.ordering_agent = OrderingAgent(MCP_TOOLS)
    st.session_state.scheduling_agent = SchedulingAgent()

st.sidebar.header("📋 Menu")

st.sidebar.subheader("🍕 Pizzas")
st.sidebar.write("• Margherita (Small / Medium / Large)")
st.sidebar.write("• Pepperoni (Medium / Large)")
st.sidebar.write("• Farmhouse (Medium / Large)")
st.sidebar.write("• Veg Supreme (Medium / Large)")
st.sidebar.write("• Chicken BBQ (Medium / Large)")
st.sidebar.write("• Paneer Tikka (Medium / Large)")

st.sidebar.markdown("---")

st.sidebar.subheader("🧀 Add-ons")
st.sidebar.write("• Extra Cheese")
st.sidebar.write("• Olives")
st.sidebar.write("• Jalapeños")
st.sidebar.write("• Mushrooms")

st.sidebar.markdown("---")

st.sidebar.subheader("🥤 Beverages")
st.sidebar.write("• Coke")
st.sidebar.write("• Sprite")
st.sidebar.write("• Water")

st.sidebar.markdown("---")
st.sidebar.write("Powered by Groq + MCP")

user_input = st.text_input(
    "What would you like to order?",
    placeholder="Order pizza, add extra cheese, make it large..."
)

if st.button("Send"):
    if not user_input.strip():
        st.warning("Please enter something")
    else:
        result = st.session_state.ordering_agent.handle(user_input)

        details = result["details"]
        st.success("Order updated")

        st.write(f"**Order ID:** {result['order_id']}")
        st.write(f"**Pizza:** {details['pizza']}")
        st.write(f"**Size:** {details['size']}")
        st.write(f"**Add-ons:** {', '.join(details['addons']) if details['addons'] else 'None'}")
        st.write(f"**ETA:** {details['eta']}")

        st.session_state.scheduling_agent.receive(result)
