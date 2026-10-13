"""Repository specialist handler."""
import re
from mcp_server.github_tools import get_repository, extract_owner_repo

def answer_repository_question(question: str, live: bool = False) -> str:
    pair = extract_owner_repo(question)
    if not pair:
        return ("Please include a repository in owner/name format, "
                "for example: octocat/Hello-World.")
    owner, repo = pair
    data = get_repository(owner, repo, live=live)
    if not data:
        return f"Could not find repository information for {owner}/{repo}."
    return (
        f"Repository: {data['full_name']}\n"
        f"Description: {data.get('description') or 'No description provided'}\n"
        f"Stars: {data.get('stargazers_count', 0)}\n"
        f"Forks: {data.get('forks_count', 0)}\n"
        f"Open issues: {data.get('open_issues_count', 0)}\n"
        f"Default branch: {data.get('default_branch', 'unknown')}\n"
        f"Data source: {data.get('source', 'unknown')}"
    )
