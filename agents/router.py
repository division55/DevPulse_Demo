"""Lightweight rule-based router for the educational demo."""
def route_question(question: str) -> str:
    q = question.lower()
    if any(word in q for word in ("release", "version", "latest tag")):
        return "release"
    if any(word in q for word in ("issue", "bug", "triage")):
        return "issue_triage"
    if any(word in q for word in ("repo", "repository", "github", "owner", "stars", "forks")):
        return "repository"
    return "general"
