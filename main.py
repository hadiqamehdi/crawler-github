from crawler import crawl_repos
from db import setup_db, upsert_repos

def main():
    setup_db()
    repos = crawl_repos(limit=1000)  # increase later
    upsert_repos(repos)
    print(f"Stored {len(repos)} repositories")

if __name__ == "__main__":
    main()
