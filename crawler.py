import base64
import re

def extract_numeric_id(base64_id):
    """Extract numeric ID from GitHub's Base64-encoded ID string."""
    try:
        # Decode the Base64 string
        decoded = base64.b64decode(base64_id).decode('utf-8')
        # Extract the numeric part - format is usually like "01:Repository132750724"
        # The pattern is: Repository followed by numbers
        match = re.search(r'Repository(\d+)', decoded)
        if match:
            return int(match.group(1))
    except Exception as e:
        print(f"Error decoding ID {base64_id}: {e}")
    # Fallback: return hash of the string
    return hash(base64_id)

def crawl_repos(limit=1000):
    repos = []
    cursor = None

    while len(repos) < limit:
        query = f"""
        {{
          search(query: "stars:>0", type: REPOSITORY, first: 100{f', after: "{cursor}"' if cursor else ''}) {{
            edges {{
              node {{
                ... on Repository {{
                  id
                  name
                  url
                  stargazerCount
                  owner {{ login }}
                }}
              }}
            }}
            pageInfo {{
              endCursor
              hasNextPage
            }}
          }}
        }}
        """

        data = run_query(query)
        edges = data["data"]["search"]["edges"]

        for e in edges:
            r = e["node"]
            # Extract numeric ID from Base64
            numeric_id = extract_numeric_id(r["id"])
            
            repos.append({
                "repo_id": numeric_id,
                "name": r["name"],
                "owner": r["owner"]["login"],
                "stars": r["stargazerCount"],
                "url": r["url"]
            })

        page = data["data"]["search"]["pageInfo"]
        if not page["hasNextPage"]:
            break

        cursor = page["endCursor"]

    return repos[:limit]