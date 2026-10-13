"""Illustrative GitHub tool layer; uses live public API or local sample data."""
import json
import re
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "sample_repositories.json"

def extract_owner_repo(text: str):
    """Return the first owner/repository pair found in text."""
    match = re.search(r"\b([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)\b", text)
    return (match.group(1), match.group(2)) if match else None

def get_repository(owner: str, repo: str, live: bool = False):
    """Get repository metadata from sample data or GitHub's public REST API."""
    if not live:
        sample = json.loads(DATA_PATH.read_text(encoding="utf-8"))
        key = f"{owner}/{repo}".lower()
        for item in sample:
            if item["full_name"].lower() == key:
                item = dict(item)
                item["source"] = "local sample data"
                return item
        return None

    url = f"https://api.github.com/repos/{owner}/{repo}"
    request = Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "DevPulse-Educational-Demo"
    })
    try:
        with urlopen(request, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
            data["source"] = "GitHub REST API"
            return data
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
        return None
