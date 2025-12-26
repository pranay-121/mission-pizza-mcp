# mission-pizza-mcp

# Mission Pizza – MCP & Agent-Based System

This project demonstrates how traditional pizza APIs can be made
accessible to AI agents using an MCP-style tool interface.

## Project Overview
AI agents act as the primary interface for ordering pizza.
The system exposes pizza operations as MCP-style tools and
uses cooperating agents to complete an end-to-end workflow.

## Tech Stack
- Python
- Groq LLM
- Streamlit
- MCP-style tool abstraction

## Setup Instructions
1. Clone the repository
2. Create a `.env` file and add:
   GROQ_API_KEY=your_api_key_here
3. Install dependencies:
   pip install -r requirements.txt
4. Run the application:
   streamlit run app.py

## How It Works
- User interacts through Streamlit UI
- Ordering agent uses Groq to understand intent
- MCP tools handle order placement
- Scheduling agent coordinates order updates

## Notes
- Backend is mocked as allowed in the problem statement
- Focus is on MCP transformation and agent coordination
