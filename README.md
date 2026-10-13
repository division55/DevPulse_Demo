# DevPulse — Educational Demonstration

DevPulse is a small educational prototype inspired by the course-project brief. It demonstrates:
- routing a GitHub-related question to a specialist handler;
- a small mock-data response path that works without API credentials;
- an optional live GitHub REST API lookup for public repository metadata;
- a basic A2A-style agent card as a descriptive JSON document.

## Important scope note
This is a **small demonstration**, not a complete reproduction of the full course capstone. It does not implement a production MCP server, LangGraph orchestration, or a full A2A transport/service. The `mcp_server/` folder contains a simple tool layer illustrating the separation of GitHub operations from routing logic.

## Requirements
- Python 3.10+
- Internet only for live GitHub lookup (optional)

## Run locally
```bash
python main.py
```

Choose demo mode to use local sample data, or live mode to request public GitHub repository metadata from GitHub's REST API.

## Example questions
- `show repository info for octocat/Hello-World`
- `find repository for fastapi`
- `show latest release for pallets/flask`

## Live API
The live mode uses Python's standard-library `urllib`; no personal access token is required for basic public repository metadata. GitHub may rate-limit unauthenticated requests. Never commit access tokens or passwords.

## Structure
- `main.py` — command-line entry point and router
- `agents/` — specialist handlers
- `mcp_server/` — illustrative GitHub tool functions
- `a2a/agent_card.json` — descriptive agent capability card
- `tests/` — unit tests for routing and handlers

## Attribution
Prepared as an independent educational demo inspired by the DevPulse course-project brief. It should not be represented as the original course implementation.
