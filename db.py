import os
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import insert
from models import metadata, repositories
from datetime import datetime

DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL)

def setup_db():
    metadata.create_all(engine)

def upsert_repos(repos):
    with engine.connect() as conn:
        for repo in repos:
            stmt = insert(repositories).values(
                repo_id=repo["repo_id"],
                name=repo["name"],
                owner=repo["owner"],
                url=repo["url"],
                stars=repo["stars"],
                last_updated=datetime.utcnow()
            ).on_conflict_do_update(
                index_elements=["repo_id"],
                set_={
                    "stars": repo["stars"],
                    "last_updated": datetime.utcnow()
                }
            )
            conn.execute(stmt)
