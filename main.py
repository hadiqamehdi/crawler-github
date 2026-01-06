from crawler import crawl_repos
from db import setup_db, upsert_repos
import sys

def main():
    try:
        setup_db()
        repos = crawl_repos(limit=1000)  # increase later
        upsert_repos(repos)
        print(f"Stored {len(repos)} repositories")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()