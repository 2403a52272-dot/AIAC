import json
import sys
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

#!/usr/bin/env python3
"""
task1.py - Simple GET request to a public API and pretty-print JSON.
Fetches posts from JSONPlaceholder and prints formatted JSON.
"""


URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_with_requests(url):
    try:
        import requests
    except ImportError as e:
        raise RuntimeError("requests library is not installed") from e
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()
def fetch_with_urllib(url):
    req = Request(url, headers={"User-Agent": "python-urllib/3"})
    try:
        with urlopen(req, timeout=10) as r:
            body = r.read()
    except (HTTPError, URLError) as e:
        raise RuntimeError(f"HTTP error: {e}") from e
    return json.loads(body.decode("utf-8"))

def main():
    try:
        # Validate URL format
        from urllib.parse import urlparse
        parsed_url = urlparse(URL)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError("Invalid URL format.")
        
        try:
            data = fetch_with_requests(URL)
        except Exception:
            # fallback if requests isn't installed or fails
            data = fetch_with_urllib(URL)
    except Exception as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        sys.exit(1)

    # Pretty-print JSON (not raw)
    print(json.dumps(data, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    try:
        u = input("Enter URL (press Enter for default https://jsonplaceholder.typicode.com/posts): ").strip()
    except EOFError:
        u = ""
    if u:
        URL = u
    try:
        main()
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)