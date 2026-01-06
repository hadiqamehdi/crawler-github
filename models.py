from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData
from datetime import datetime

metadata = MetaData()

repositories = Table(
    "repositories",
    metadata,
    Column("repo_id", String, primary_key=True),  # Changed from BigInteger to String
    Column("name", String),
    Column("owner", String),
    Column("url", String),
    Column("stars", Integer),
    Column("last_updated", TIMESTAMP, default=datetime.utcnow),
)