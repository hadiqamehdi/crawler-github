from github_client import run_query

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
            repos.append({
                "repo_id": r["id"],  # Keep as string (Base64)
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