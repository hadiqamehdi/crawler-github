from sqlalchemy import Table, Column, Integer, String, BigInteger, TIMESTAMP, MetaData
from datetime import datetime

metadata = MetaData()

repositories = Table(
    "repositories",
    metadata,
    Column("repo_id", BigInteger, primary_key=True),
    Column("name", String),
    Column("owner", String),
    Column("url", String),
    Column("stars", Integer),
    Column("last_updated", TIMESTAMP, default=datetime.utcnow),
)
