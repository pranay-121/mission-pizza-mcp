# mission-pizza-mcp

# Mission Pizza – MCP & Agent System

This project demonstrates how traditional pizza APIs can be exposed
to AI agents using an MCP-style tool interface.

## What it does
- Converts pizza capabilities into MCP-style tools
- Uses a Groq-powered ordering agent to understand natural language
- Uses a second agent to coordinate order updates
- Provides a Streamlit UI for live demonstration

## Tech Used
- Python
- Groq LLM
- Streamlit
- MCP-style tool abstraction

## How to Run
1. Add your Groq API key in a `.env` file
2. Install dependencies:
   pip install -r requirements.txt
3. Run:
   streamlit run app.py

## Notes
- Backend is mocked as allowed in the problem statement
- Focus is on MCP, agents, and orchestration
