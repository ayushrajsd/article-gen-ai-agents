import os
from crewai.tools import tool
from serpapi import GoogleSearch


@tool("Google Search")
def search_tool(query: str) -> str:
    """Search Google for current articles and news using SerpApi.
    Returns titles, URLs, and snippets for the top results."""
    params = {
        "q": query,
        "api_key": os.getenv("SERPAPI_API_KEY"),
        "num": 5,
    }
    results = GoogleSearch(params).get_dict()
    organic = results.get("organic_results", [])
    if not organic:
        return "No results found."

    lines = []
    for r in organic:
        lines.append(
            f"Title: {r.get('title')}\n"
            f"URL: {r.get('link')}\n"
            f"Snippet: {r.get('snippet')}\n"
        )
    return "\n".join(lines)
