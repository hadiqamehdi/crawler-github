# GitHub Repository Crawler

A scalable GitHub repository crawler that uses GitHub’s GraphQL API to collect
repository star counts and store them in PostgreSQL.

The system is designed to scale to 100,000 repositories, while the GitHub Actions
pipeline runs with a smaller configurable limit to respect CI execution constraints.

## Features
- Uses GitHub GraphQL API with cursor-based pagination
- Handles rate limits with retry and backoff
- Stores data in PostgreSQL using efficient upsert operations
- Designed for daily incremental re-crawling
- Runs automatically via GitHub Actions
- Exports a PostgreSQL database dump as a pipeline artifact

## Architecture Overview
- `github_client.py`: Anti-corruption layer for GitHub GraphQL API
- `crawler.py`: Stateless crawling and pagination logic
- `db.py`: Database schema setup and upsert logic
- `main.py`: Application orchestration
- GitHub Actions: End-to-end automated pipeline with PostgreSQL service container

## GitHub Actions Pipeline
The workflow:
1. Starts a PostgreSQL service container
2. Initializes database schema
3. Crawls GitHub repositories via GraphQL API
4. Stores and updates star counts in PostgreSQL
5. Dumps database contents and uploads as an artifact

The pipeline uses the default GitHub Actions token and does not require
any elevated permissions or private secrets.

## Scaling Considerations
- Each GraphQL request retrieves up to 100 repositories
- Crawling 100,000 repositories requires ~1,000 API requests
- The crawler is idempotent and safe to run daily
- Schema supports efficient incremental updates

## Running Locally (Optional)
```bash
pip install -r requirements.txt
export GITHUB_TOKEN=<your_token>
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/github_db
python main.py
