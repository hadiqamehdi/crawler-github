from crawler import crawl_repos
from db import setup_db, upsert_repos
import sys
import traceback

def main():
    try:
        print("Setting up database...")
        setup_db()
        print("Crawling repositories...")
        repos = crawl_repos(limit=100)  # Start with 100 for testing
        print(f"Crawled {len(repos)} repositories")
        print("Upserting to database...")
        upsert_repos(repos)
        print(f"Successfully stored {len(repos)} repositories")
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()