# GitHub Repository Crawler

Crawls 100,000 GitHub repositories and stores star counts in PostgreSQL.

## Features
- Uses GitHub GraphQL API for efficient data retrieval
- Handles rate limits with exponential backoff
- Stores data in PostgreSQL with efficient upsert operations
- Exports data to CSV
- Runs as a GitHub Actions workflow

## Setup

1. **Create a GitHub Personal Access Token:**
   - Go to https://github.com/settings/tokens
   - Generate token with `repo` scope

2. **Local Testing:**
```bash
# Clone repository
git clone <your-repo-url>
cd github-crawler

# Install dependencies
pip install -r requirements.txt

# Set environment variable
export GITHUB_TOKEN="your_token_here"

# Run locally (uses SQLite)
python main.py