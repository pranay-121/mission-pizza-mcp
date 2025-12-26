## Architectural Choices

The system is designed around agent-based interaction.
Instead of exposing traditional REST APIs directly to users,
pizza capabilities are abstracted as MCP-style tools.

A lightweight mock backend is used to keep focus on
agent orchestration and MCP usage rather than REST complexity.

Groq is used as the LLM for fast and reliable intent extraction.
Streamlit is used only as a demonstration layer.


## Design Assumptions

- Only one active order per user session
- Orders are modified incrementally through conversation
- Backend persistence is not required for this challenge
- Agents are trusted to coordinate via in-memory state

## Handling Ambiguities

User input may be incomplete or vague.
To handle this, the ordering agent applies safe defaults:
- Default pizza: Margherita
- Default size: Medium

If the user adds information later (e.g. add-ons or size),
the existing order is updated instead of creating a new one.
This mirrors real conversational ordering behavior.
