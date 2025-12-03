
import os, re
from crewai.tools import tool

import requests

@tool
def web_search_tool(query: str):
  """
    Web search tool using Firecrawl API.
    Args:
      query: The query to search for.
    Returns:
      A list of search results.
      Each result contains:
        - title: The title of the search result.
        - url: The URL of the search result.
        - markdown: The markdown content of the search result.
  """
  # Check if environment variables are set
  api_key = os.getenv('FIRECRAWL_API_KEY')
  api_url = os.getenv('FIRECRAWL_API_URL')
  
  if not api_key or not api_url:
    return f"Error: Missing environment variables. FIRECRAWL_API_KEY: {bool(api_key)}, FIRECRAWL_API_URL: {bool(api_url)}"
  
  payload = {
    "query": query,
    "sources": ["web"],
    "categories": [],
    "limit": 5,
    "scrapeOptions": {
    "onlyMainContent": True,
    "maxAge": 172800000,
    "parsers": ["pdf"],
    "formats": ["markdown"],
    },
  }

  headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
  }

  response = requests.post(api_url, json=payload, headers=headers)
  response = response.json()
  
  if not response["success"] :
    return "Error using tool."

  cleaned_chunks =[]

  for result in response["data"]["web"]:
    title = result["title"]
    url = result["url"]
    markdown = result["markdown"] if "markdown" in result else ""

    # Remove HTML tags including <br>, <p>, etc.
    cleaned = re.sub(r"<[^>]+>", "", markdown)
    # Remove extra whitespace and newlines
    cleaned = re.sub(r"\\+|\n+|\s+", " ", cleaned).strip()
    # Remove markdown links and URLs
    cleaned = re.sub(r"\[[^\]]+\]\([^\)]+\)|https?://[^\s]+", "", cleaned)

    cleaned_result = {
      "title": title,
      "url": url,
      "markdown": cleaned,
    }

    cleaned_chunks.append(cleaned_result)

  return cleaned_chunks















